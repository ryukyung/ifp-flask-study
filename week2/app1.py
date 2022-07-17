from flask import Flask, url_for, request
app = Flask(__name__)

topics = [
    {'id': 1, 'title': '짱구는 못말려', 'character': '짱구', 'startYear': 1990},
    {'id': 2, 'title': '도라에몽', 'character': '도라에몽', 'startYear': 1969},
]


# 사용자가 어떤 경로를 입력하지 않고 접속하면 인덱스 함수가 응대하라고 담당자를 지정한 것
@app.route('/')
def index():
    return 'Welcome!'


# /hi/<username>로 접속했을 때 hi() 함수가 응대해서 hi, {username}를 응답한다
@app.route('/hi/<username>')
def hi(username):
    return f'Hi, {username}'


# 슬래시가 있을 때
@app.route('/login/')
def login():
    return 'The login page'


# 슬래시가 없을 때
@app.route('/logout')
def logout():
    return 'the logout page'


with app.test_request_context():
    print(url_for('index'))                    # /
    print(url_for('hi', username='ryukyung'))  # /hi/ryukyung
    print(url_for('login'))                    # /login
    print(url_for('login', next='/'))          # /login/?next=%F
    print(url_for('logout'))                   # /logout


app.run(port=5001, debug=True)
