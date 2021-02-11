"""
The emails blueprint handles everything related to the web application - uploading email lists, viewing email lists, downloading sanitized email list, etc
"""

from flask import Blueprint

emails_blueprint = Blueprint('emails', __name__)

from . import views

    