from flask import Flask
import os
import logging
from logging.handlers import RotatingFileHandler
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



def create_app():
    """
    Instantiate a flask application, configure its environment varables, initialise all flask extensions, register blueprints and request callbacks, configure logging 
    """
    app = Flask(__name__)

    #configure flask app
    config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(config_type)

    #register blueprints
    register_blueprints(app)

    #initialize flask extensions 
    initialize_extensions(app)

    #configure the logger
    configure_logging(app)

    #call request callbacks function
    register_app_callbacks(app)

    #call error handler function
    register_error_pages(app)

    return app



##### Helper Functions #####

def register_blueprints(app):
    """

    Import and register blueprints

    """
    from project.emails import emails_blueprint
    from project.auth import auth_blueprint
    app.register_blueprint(emails_blueprint)
    app.register_blueprint(auth_blueprint)

def initialize_extensions(app):
    """
    Initialize all flask extensions to be used in the application: Once a flask application instance has been created, it is passed to each flask extension to bind the flask extension to the flask instance. 
    """
    db = SQLAlchemy()
    db_migration = Migrate()

    db.init_app(app)
    db_migration.init_app(app, db)


def configure_logging(app):
    """
    Configure logging for the flask application.
    Creates a new handler for writing the log messages to the specified file. 
    A new log file is created whenever the current log file gets close to a specified file size. Up to 20 log files can be saved before the log files are overwritten.
    To specify format of log messages, creates a Formatter object and adds this object (file_formatter) to the handler.
    Sets the logging level desired (INFO upwards)
    Adds this file handler to the app.logger object, which is used to create log messages.
    """
    file_handler = RotatingFileHandler('instance/scrub-my-list.log', maxBytes=16384, backupCount=20)
    file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s:%(lineno)d]')
    file_handler.setFormatter(file_formatter) 
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Starting the Scrub My List App...')


def register_app_callbacks(app):
    """
    Register all the request callback functions to be used in the application
    """
    pass


def register_error_pages(app):
    """
    Register the error handler functions for custom error pages (error functions not tied to a specific blueprint)
    """
    pass