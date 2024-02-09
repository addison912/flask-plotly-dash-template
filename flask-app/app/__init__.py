from flask import Flask
from flask_assets import Environment
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config.Config")
assets = Environment()
assets.init_app(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

with app.app_context():
    from app import routes
    from .assets import compile_static_assets

# Import your app
    from .dash_apps.test_app import my_app
    from .dash_apps.iris_app import iris_kmeans
    from .dash_apps.example_app import dash_home

# Initialize your app
    app = my_app.init_dash(app) 
    app = iris_kmeans.init_dash(app)
    app = dash_home.init_dash(app)
    

# Compile static assets
compile_static_assets(assets)