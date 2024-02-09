"""Flask config."""
from os import environ, path
from dotenv import load_dotenv

# from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"), override=True)


class Config:
    """Flask configuration variables."""

    # General Config
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")
    SECRET_KEY = environ.get("SECRET_KEY")
    DEBUG = environ.get("FLASK_DEBUG")

    # Assets
    ASSETS_DEBUG = environ.get("ASSETS_DEBUG")

    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    COMPRESSOR_DEBUG = environ.get("COMPRESSOR_DEBUG")

    # DB
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost},{dbport}/{dbname}'.format(
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}:{dbport}/{dbname}'.format(
        dbuser=environ.get('DBUSER'),
        dbpass=environ.get('DBPASS'),
        dbhost=environ.get('DBHOST'),
        dbname=environ.get('DBNAME'),
        dbport=environ.get('DBPORT')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    DEFAULT_ERROR_MESSAGE = "The server encountered an error!"
    
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = environ.get('VERIFICATION_EMAIL')
    MAIL_PASSWORD = environ.get('VERIFICATION_EMAIL_PASS')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

