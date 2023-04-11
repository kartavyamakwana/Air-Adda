from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__)

app.config['SECRET_KEY'] = '5cb5d3d21d947a5654439fc4726e173b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Integration%4023@localhost:3306/this'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.app_context().push()
loginManager = LoginManager(app)

from airline import routes
