from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'James'}
    posts = [
        {
            'author': {'username': 'Sophie'},
            'body': 'Chippys!'
        },
        {
            'author': {'username': 'BorBor'},
            'body': 'Hello, Sophie!'
        },
        {
            'author': {'username': 'Bertie'},
            'body': 'What\'s for dinner BorBor?'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
