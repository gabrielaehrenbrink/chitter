import os
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from lib.database_connection import get_flask_database_connection
from lib.post_repository import PostRepository
from lib.account_repository import AccountRepository
from lib.account_validator import AccountParametersValidator
from lib.account import Account
from lib.post import Post


def load_user(user_id):
    connection = get_flask_database_connection(app)
    repository = AccountRepository(connection)
    return repository.find_by_id(user_id)

app = Flask(__name__)
app.secret_key = 'SECRET_KEY' 
login_manager = LoginManager(app)
login_manager.login_view = 'get_login'
login_manager.user_loader(load_user) 



@app.route('/', methods=['GET', 'POST'])
def get_homepage():
    if request.method == 'POST':
        username = request.form['username']
        user_password = request.form['user_password']

        connection = get_flask_database_connection(app)
        repository = AccountRepository(connection)
        account = repository.authenticate(username, user_password)

        if account:
            login_user(Account(account.id, account.username, account.email, account.user_password))
            return redirect(url_for('get_posts'))
        else:
            flash('Invalid username or password. Please try again.')

    return render_template("index.html")

@app.route('/posts', methods=['GET'])
def get_posts():
    connection = get_flask_database_connection(app)
    repository = PostRepository(connection)
    posts = repository.all() 
    return render_template("posts.html", posts=posts) 


@app.route('/newaccount', methods=['GET'])
def get_new_account():
    return render_template("new_account.html")  

@app.route('/newaccount', methods=['POST'])
def create_new_account():
    username = request.form['username']
    email = request.form['email']
    user_password = request.form['user_password']
    confirm_password = request.form['confirm_password']

    errors = []

    if not username:
        errors.append('Username is required')
    if not email:
        errors.append('Email is required')
    if not user_password:
        errors.append('Password is required')
    if user_password != confirm_password:
        errors.append('Passwords do not match')

    # Only validate password and email formats if they are not empty
    if email and user_password:
        account_parameters_validator = AccountParametersValidator(username, email, user_password)
        if not account_parameters_validator.is_valid():
            errors.extend(account_parameters_validator.generate_errors())

    if errors:
        return render_template('new_account.html', errors=errors)
    
    # Proceed with account creation if no errors
    connection = get_flask_database_connection(app)
    repository = AccountRepository(connection)
    account = Account(None, username, email, user_password)
    repository.create(account)
        
    return redirect(url_for('get_login'))



@app.route('/login', methods=['GET', 'POST'])
def get_login():
    if request.method == 'POST':
        username = request.form['username']
        user_password = request.form['user_password']

        connection = get_flask_database_connection(app)
        repository = AccountRepository(connection)
        account = repository.authenticate(username, user_password)

        if account:
            login_user(Account(account.id, account.username, account.email, account.user_password))
            return redirect(url_for('get_posts'))
        else:
            flash('Invalid username or password. Please try again.')
    return render_template("login.html")  


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_homepage'))


@app.route('/newpost', methods=['GET', 'POST'])
@login_required
def new_post():
    chars_left = 150
    if request.method == 'POST':
        username = current_user.username
        content = request.form['textInput']

        connection = get_flask_database_connection(app)
        repository = PostRepository(connection)
        post = Post(None, content, username)
        repository.create(post)

        posts = repository.all()
        
        return render_template("posts.html", posts=posts)

    return render_template('new_post.html', chars_left=chars_left)


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
