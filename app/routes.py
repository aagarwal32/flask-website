from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Jumpstart')

@app.route('/discover')
def discover():
    return render_template('discover.html', title='Discover')

@app.route('/contribute')
def contribute():
    return render_template('contribute.html', title='Contribute')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))

    return render_template('login.html', title='Login up', form=form)

