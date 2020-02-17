from flask import render_template
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
