from flask import current_app, Blueprint, render_template
from app.database import db_session
from app.event.models import EventModel, MemberModel

main = Blueprint('main', __name__)
Session = db_session()


@main.route("/")
def index():
    try:
        obj = Session.query(EventModel).filter(
            EventModel.members).order_by(EventModel.event_id.desc()).all()
    except Exception as e:
        return "Database connection failed, Please contact your administrator."

    context = {
        'obj': obj,
    }
    return render_template('home.html', title='Welcome to JFlask', context=context)
