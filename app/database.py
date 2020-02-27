from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, create_session
from sqlalchemy.ext.declarative import declarative_base


engine = None
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()


def init_engine(uri, **kwargs):
    global engine
    engine = create_engine(uri, **kwargs)
    return engine


def init_db():
    from app.event.models import EventModel, MemberModel
    Base.metadata.create_all(bind=engine)
