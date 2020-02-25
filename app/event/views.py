from flask import current_app, Blueprint, render_template, flash, redirect
from app.database import db_session
from .models import EventModel, MemberModel
from .form import FormEvent, FormMember

event = Blueprint('event', __name__)
Session = db_session()


@event.route('/save_emails', methods=['GET', 'POST'])
def save_emails():
    form = FormEvent()
    try:
        # Select member_id and username to populate the choice
        form.member.choices = [(m.member_id, m.username)
                               for m in Session.query(MemberModel).all()]
    except Exception as e:
        return "Database connection failed, Please contact your administrator."

    if form.validate_on_submit():
        event_data = EventModel(
            email_subject=form.email_subject.data,
            email_content=form.email_content.data,
            timestamp=form.timestamp.data
        )
        try:
            # Save the relation between event and members
            for member in form.member.data:
                qs = Session.query(MemberModel).filter(
                    MemberModel.member_id == member).first()
                event_data.members.append(qs)

            Session.add(event_data)
            Session.commit()
            flash('Email saved with Subject: {}, Content: {}'.format(
                form.email_subject.data, form.email_content.data))
            return redirect("/")
        except Exception as e:
            Session.rollback()
            return "Data saving failed, Please try again"
    return render_template('save_emails.html', title='Save Emails', form=form)


@event.route('/add_member', methods=['GET', 'POST'])
def add_member():
    form = FormMember()
    if form.validate_on_submit():
        flash('Member with username: {}, Sucessfuly added.'.format(
            form.username.data))
        member_data = MemberModel(
            email=form.email.data,
            username=form.username.data
        )
        try:
            # Saving data member
            Session.add(member_data)
            Session.commit()
        except Exception as e:
            Session.rollback()
            flash("Data saving failed, Please try again")
        return redirect("/")
    return render_template('add_member.html', title='Add Member', form=form)
