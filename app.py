from flask import Flask,render_template, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user, LoginManager
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

# configure login
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# login manager
@login_manager.user_loader  # noqa: F821
def load_user(user_id):
     with Session(db.engine) as session:
         return session.ger(User, int(user_id))

@app.route('/')
@login_required()
def index():
   if not current_user.is_authenticated:
        return redirect(url_for('login'))
   return render_template('index.html', title='Dashboard', current_user=current_user.username)
