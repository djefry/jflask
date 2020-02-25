import flask
import pytest_flask_sqlalchemy
from app.database import db_session
from app.event.models import EventModel, MemberModel


def test_app(app):
    assert isinstance(app, flask.Flask)


def test_a_transaction(db_session):
    row = db_session.query(EventModel).get(1)
    row.name = 'testing'

    db_session.add(row)
    db_session.commit()


def test_transaction_doesnt_persist(db_session):
    row = db_session.query(EventModel).get(1)
    assert row.name != 'testing'
