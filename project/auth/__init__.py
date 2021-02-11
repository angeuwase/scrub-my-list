"""
The auth blueprint handles everything related to user management- user registration, user login, user logout, user profile for changing credentials

"""

from flask import Blueprint

auth_blueprint = Blueprint('auth', __name__)

from . import views

