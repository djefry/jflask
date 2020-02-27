# App configuration
class ConfigTest:
    # Set database URI for testing
    SQLALCHEMY_DATABASE_URI = 'postgresql:///test?client_encoding=utf8'
    # Enable debug mode
    DEBUG = True
    # Enable test
    TESTING = True

    # Secret Key
    SECRET_KEY = 'secret'

    # Mail configuration
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_MAX_EMAILS = 1
    MAIL_USERNAME = '4ef0a76264776f'
    MAIL_PASSWORD = '9772f11bff889a'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    # Celery configuration
    CELERY_BROKER_URL = 'redis://redis:6379/0'
    CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
    CELERYBEAT_SCHEDULE = {
        # Executes every minute
        'execute-every-60-seconds': {
            'task': 'periodic_task',
            'schedule': 60.0,
        }
    }
