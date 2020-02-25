import pytest
from test_settings import ConfigTest
from app import create_app
from app.database import db_session, init_db, init_engine


@pytest.fixture
def app():
    """
    Creates a new Flask application for a test duration.
    Uses application factory `create_app`.
    """
    app = create_app(ConfigTest)
    return app


@pytest.fixture(scope='session')
def database(request):
    '''
    Create a Postgres database for the tests, and drop it when the tests are done.
    '''
    pg_host = "localhost"
    pg_port = "5432"
    pg_user = "wandashare"
    pg_db = "test"

    init_postgresql_database(pg_user, pg_host, pg_port, pg_db)
    print(init_postgresql_database(pg_user, pg_host, pg_port, pg_db))

    @request.addfinalizer
    def drop_database():
        drop_postgresql_database(pg_user, pg_host, pg_port, pg_db, 11.7)


@pytest.fixture(scope='session')
def app(database):
    '''
    Create a Flask app context for the tests.
    '''
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONN

    return app


@pytest.fixture(scope='session')
def _db(app):
    '''
    Provide the transactional fixtures with access to the database via a Flask-SQLAlchemy
    database connection.
    '''
    db = SQLAlchemy(app=app)

    return db
