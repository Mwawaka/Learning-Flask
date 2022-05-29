from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '44de154f207a4c739f20ec82d91c8474d6c139402e5cb11473920dae31e57d0d'
bcrypt = Bcrypt(app)
login_manager=LoginManager(app)

from market import routes