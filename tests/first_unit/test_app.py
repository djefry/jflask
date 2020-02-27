from flask import Flask
from celery import Celery
from app.event.models import MemberModel


# Application factory test
def test_app(app):
    assert isinstance(app, Flask)


# Celery application testing
def test_celery(celery_app):
    assert isinstance(celery_app, Celery)


# Database insert test
def test_a_transaction(_db_session):
    row = MemberModel(
        email='testing',
        username='testing'
    )

    _db_session.add(row)
    _db_session.commit()

# Database select test get available data


def test_transaction_persist(_db_session):
    row = _db_session.query(MemberModel).first()
    assert str(row.email) == 'testing'


# Database select test get empty data
def test_transaction_empty(_db_session):
    row = _db_session.query(MemberModel).get(2)
    assert row == None
