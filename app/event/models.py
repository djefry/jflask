from sqlalchemy import (
    ForeignKey, Column, Integer,
    Text, String, DateTime, Table
)
from sqlalchemy.orm import relationship, backref
from app.database import Base


class EventModel(Base):
    __tablename__ = 'events'

    event_id = Column(Integer(), primary_key=True)
    email_subject = Column(Text(100), nullable=False)
    email_content = Column(Text(1000), nullable=False)
    timestamp = Column(DateTime(), nullable=False)
    members = relationship('MemberModel', secondary='event_member_link')

    # Representation
    def __repr__(self):
        return '<Event model {}>'.format(self.event_id)


class MemberModel(Base):
    __tablename__ = 'members'

    member_id = Column(Integer(), primary_key=True)
    email = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)

    # Relationships
    events = relationship(
        'EventModel', secondary='event_member_link')

    # Representation
    def __repr__(self):
        return '<Member model {}'.format(self.member_id)


class EventMemberLinkModel(Base):
    __tablename__ = 'event_member_link'
    event_id = Column(Integer, ForeignKey(
        'events.event_id'), primary_key=True)
    member_id = Column(Integer, ForeignKey(
        'members.member_id'), primary_key=True)
