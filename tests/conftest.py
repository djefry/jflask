import pytest
import pytest_html
from test_settings import ConfigTest
from app import create_app
from app.database import db_session
from sqlalchemy_utils import drop_database
from selenium import webdriver


@pytest.fixture(scope='session')
def app():
    """
    Creates a new Flask application for a test duration.
    Uses application factory `create_app`.
    """
    app = create_app(ConfigTest)
    yield app


@pytest.fixture(scope='session')
def _db_session():
    """
    Create Session for test transactional database
    """
    Session = db_session()
    yield Session


# Fixture for Chrome
@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome()
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    """Cleanup once we are finished."""
    def drop_db():
        drop_database(ConfigTest.SQLALCHEMY_DATABASE_URI)
    request.addfinalizer(drop_db)
