from flask import Flask
from app.database import init_engine, init_db

# Initialize db without configuring
#db = SQLAlchemy()


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

    # Initialize any extension and bind blueprint
    from .main.views import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .event.views import event as event_blueprint
    app.register_blueprint(event_blueprint)

    return app
