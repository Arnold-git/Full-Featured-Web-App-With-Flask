from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager




app = Flask(__name__)
app.config['SECRET_KEY'] = 'c61d0b0167fa2d8681a9f80c56b4bc2a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager =  LoginManager(app)

from flaskblog import routes