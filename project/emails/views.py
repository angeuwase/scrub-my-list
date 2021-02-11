from . import emails_blueprint
from flask import render_template


@emails_blueprint.route('/')
def index():
    return render_template('emails/index.html')


@emails_blueprint.route('/view_lists/')
def view_lists():
    return render_template('emails/view_lists.html')


@emails_blueprint.route('/upload_list')
def upload_list():
    return render_template('emails/upload_list.html')


