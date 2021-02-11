from . import auth_blueprint
from flask import render_template

@auth_blueprint.route('/register')
def register():
    return render_template('auth/register.html')

@auth_blueprint.route('/login')
def login():
    return render_template('auth/login.html')


@auth_blueprint.route('/profile')
def profile():
    return render_template('auth/profile.html')