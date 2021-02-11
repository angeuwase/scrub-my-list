import os

# Determine the folder of the top-level directory of this project
BASEDIR = os.path.abspath(os.path.dirname(__file__))



class Config(object):
    ##### Default Environment Configuration #####
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False

    ##### Application Configuration #####
    SECRET_KEY = os.getenv('SECRET_KEY', default='Adlskn sdjddn djnd')
    MAX_CONTENT_LENGTH = 1024 * 1024 #max size of files users can upload is 1MB
    UPLOAD_EXTENSIONS = ['.csv', '.txt'] #we only accept text and csv file formats from the user otherwise raise an error

    ##### Database Configuration #####
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', default=f"sqlite:///{os.path.join(BASEDIR, 'instance', 'app.db')}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False



class ProductionConfig(Config):
    FLASK_ENV = 'production'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    
