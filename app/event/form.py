from app import setdate
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, ValidationError
from wtforms.fields.html5 import DateTimeField
from .models import MemberModel, EventModel


def date_check(form, field):
    if field.data < setdate():
        raise ValidationError("You can't set schedule to past")


class FormEvent(FlaskForm):

    email_subject = StringField('Subject', validators=[DataRequired()])
    email_content = StringField('Content', validators=[DataRequired()])
    member = SelectMultipleField(
        'Member', coerce=int, validators=[DataRequired()])
    timestamp = DateTimeField('Date Send', validators=[DataRequired(
    ), date_check], default=setdate(), format='%Y-%m-%d %H:%M')
    submit = SubmitField('Save Email')


class FormMember(FlaskForm):

    email = StringField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Save Member')
