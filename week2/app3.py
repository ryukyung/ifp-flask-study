from flask import Flask, request, redirect

app = Flask(__name__)


nextId = 4
topics = [
    {'id': 1, 'title': '짱구는 못 말려', 'character': '짱구'},
    {'id': 2, 'title': '도라에몽', 'character': 'css is ...'},
    {'id': 3, 'title': '뽀롱 뽀롱 뽀로로', 'character': '뽀로로'}
]


def template(contents, content):
    return f'''<!DOCTYPE html>
    <html>
        <body>
        <h1><a href="/">WEB</a></h1>
        <ol>
            {contents}
        </ol>
        {content}
        <ul>
            <li><a href="/create/">create</a></li>
        </ul>
        </body>
    </html>
'''


def getContents():
    liTags = ''
    for topic in topics:
        liTags = liTags + \
            f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags


@app.route('/')
def index():
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')


@app.route('/read/<int:id>/')
def read(id):
    title = ''
    character = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            character = topic['character']
            break
    return template(getContents(), f'<h2>{title}</h2>{character}')


@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><input type="text" name="character" placeholder="character"></p>
                <p><input type="submit" value="create"></p>
            </form>
        '''
        return template(getContents(), content)
    elif request.method == 'POST':
        global nextId
        title = request.form['title']
        character = request.form['character']
        newTopic = {'id': nextId, 'title': title, 'character': character}
        topics.append(newTopic)
        url = '/read/'+str(nextId)+'/'
        nextId = nextId + 1
        return redirect(url)


app.run(port=5001, debug=True)
