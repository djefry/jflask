from flask import Flask
from app.database import init_engine, init_db
from celery import Celery


def create_app(config=None):
    app = Flask(__name__)

    if config is not None:
        app.config.from_object(config)

    # Database configuration, releated to database.py
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    init_engine(app.config['SQLALCHEMY_DATABASE_URI'],
                encoding='utf8')
    init_db()
    app.config['SECRET_KEY'] = 'secret'

    # Mail configuration
    app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
    app.config['MAIL_PORT'] = 2525
    app.config['MAIL_MAX_EMAILS'] = 3
    app.config['MAIL_USERNAME'] = '4ef0a76264776f'
    app.config['MAIL_PASSWORD'] = '9772f11bff889a'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False

    # Initialize any extension and bind blueprint
    from .main.views import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .event.views import event as event_blueprint
    app.register_blueprint(event_blueprint)

    return app


def make_celery(app):
    # Celery configuration
    app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
    app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
    app.config['CELERYBEAT_SCHEDULE'] = {
        # Executes every minute
        'execute-every-60-seconds': {
            'task': 'periodic_task',
            'schedule': 30.0,
        }
    }

    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery
