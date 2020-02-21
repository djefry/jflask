from flask import current_app, Blueprint, render_template

main = Blueprint('main', __name__)


@main.route("/")
def index():
    return render_template('home.html', title='Welcome to JFlask')
