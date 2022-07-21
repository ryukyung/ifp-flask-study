# blog/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager # flask_loginManager() 로그인 준비하기
from pprint import pprint
db = SQLAlchemy()
DB_NAME="blog_db"

def create_app():
    # from .models import User
    app = Flask(__name__) # Flask app 만들기
    app.config['SECRET_KEY'] = "IFP"

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix="/blog")
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/auth')
    # from .models import User
    from .models import User
    create_database(app)
    login_manager= LoginManager() # LoginManager() 객체를 만들어준다
    login_manager.login_view = " auth.login" 
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user_by_id(id):
        return User.query.get(int(id))
    return app
def create_database(app):
    if not path.exists("blog/"+DB_NAME):
        db.create_all(app=app)
