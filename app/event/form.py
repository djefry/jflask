import datetime
from sqlalchemy import func
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateTimeField
from .models import MemberModel, EventModel


class FormEvent(FlaskForm):

    email_subject = StringField('Subject', validators=[DataRequired()])
    email_content = StringField('Content', validators=[DataRequired()])
    member = SelectMultipleField('Member', coerce=int)
    timestamp = DateTimeField('Date Send', validators=[DataRequired(
    )], default=datetime.datetime.utcnow()+datetime.timedelta(hours=8), format='%Y-%m-%d %H:%M')
    submit = SubmitField('Save Email')


class FormMember(FlaskForm):

    email = StringField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Save Member')
