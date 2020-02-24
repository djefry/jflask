from flask import Flask
import datetime
from app.database import init_engine, init_db
from celery import Celery


def create_app(config=None):
    # App Initializtion
    app = Flask(__name__)
    app.config.from_object(config)

    # Database Initialization
    init_engine(app.config['SQLALCHEMY_DATABASE_URI'],
                encoding='utf8')
    init_db()

    # Initialize any extension and bind blueprint
    from .main.views import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .event.views import event as event_blueprint
    app.register_blueprint(event_blueprint)

    return app


def make_celery(app):
    # Celery initialization
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


# Set date to UTC+8
def setdate():
    return (datetime.datetime.utcnow()+datetime.timedelta(hours=8))
