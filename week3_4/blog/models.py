# blog/models.py
from  . import db
from flask_login import UserMixin 
# flask_login 라이브러리 : 플라스크에서 로그인 기능을 쉽게 구현할 수 있도록 도와주는 라이브러리
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
