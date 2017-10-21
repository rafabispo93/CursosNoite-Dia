# -*- coding: utf-8 -*-
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from application.config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)

# Flask-Mail
mail = Mail(app)

# Flask-SQLAlchemy
db = SQLAlchemy(app)

# Flask-Migrate
migrate = Migrate(app, db)

# Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Blueprints
from application.views import errors

from application.views.app import mod_app
app.register_blueprint(mod_app)

from application.views.admin import mod_admin
app.register_blueprint(mod_admin)

from application.views.curso import mod_curso
app.register_blueprint(mod_curso)
