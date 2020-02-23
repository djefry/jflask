import datetime
from http.client import HTTPException
from app import create_app, make_celery
from sqlalchemy import and_
from celery.utils.log import get_task_logger
from app.event.models import EventModel, MemberModel
from app.database import db_session
from flask_mail import Mail, Message
from collections import defaultdict

# App initialization
app = create_app()
Session = db_session()

# Email initialization
mail = Mail(app)

# Celery initialization
logger = get_task_logger(__name__)
celery = make_celery(app)

# Async Task
@celery.task(name="async_task", auto_retry=[HTTPException], max_retries=5)
def send_email(data):
    # with app.app_context():
    with mail.connect() as conn:
        for email in data['email']:
            msg = Message(data['subject'],
                          sender="admin@jflask.com",
                          recipients=[email])
            msg.body = data['content']
            # conn.send(msg)
            logger.info("Async task complete for: {}".format(email))


# Periodic task, beat speed in setting/config
@celery.task(name="periodic_task")
def periodic_task():
    # Get time for UTC+8
    time_now = (datetime.datetime.utcnow()+datetime.timedelta(hours=8))
    # Select timestamp where email sent status false
    qs_date = Session.query(EventModel).filter(EventModel.sent == True)
    for date in qs_date:
        # Compare the timestamp with time now
        if date.timestamp <= time_now:
            # Joint EventModel and Member Model to get email address
            qs_mail = Session.query(EventModel).filter(and_(EventModel.event_id == date.event_id),
                                                       (EventModel.members)).one()
            print("Hasil Query :{}".format(qs_mail.sent))
            email_subject = qs_mail.email_subject.decode("utf-8")
            email_content = qs_mail.email_content.decode("utf-8")
            # Get email address
            data = defaultdict(list)
            for mail in qs_mail.members:
                data['email'].append(mail.email)

            data['subject'] = email_subject
            data['content'] = email_content
            # Send async email
            send_email.apply_async([data], countdown=10)
            # Change sent status to true
            qs_mail.sent = True
            Session.commit()

    # print('Time Now : {}'.format(time_now))
    logger.info("Periodic task run")


if __name__ == '__main__':
    app.run('0.0.0.0', 8000, debug=True)
