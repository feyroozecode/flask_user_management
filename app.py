from flask import Flask
from flask_login import LoginManager
from models.users import db
from sqlalchemy.orm import Session
from models.users import init_model, User

# config
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)
# init model
init_model(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

# login manager
@login_manager.user_loader  # noqa: F821
def load_user(user_id):
     with Session(db.engine) as session:
         return session.ger(User, int(user_id))

@app.route('/')
def home():
   return  "<p>Salam binevenue</p>"
