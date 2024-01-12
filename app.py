import os
from flask import Flask, request, render_template, redirect, jsonify, url_for
from flask_login import LoginManager
from lib.database_connection import get_flask_database_connection
from lib.post_repository import PostRepository
from lib.account_repository import AccountRepository
from lib.account_validator import AccountParametersValidator
from lib.account import Account
from lib.post import Post

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_homepage():
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

    errors = []

    if not username:
        errors.append('Username is required.')
    if not email:
        errors.append('Email is required.')
    if not user_password:
        errors.append('Password is required.')

    account_parameters_validator = AccountParametersValidator(username, email, user_password)
    if not account_parameters_validator.is_valid():
        errors.append('Password or email is not valid. Must enter valid email. Password must have at least 8 characters, including a letter, a number and special character')

    if errors:
        return render_template('new_account.html', errors=errors)
    
    username = request.form['username']
    email = request.form['email']
    user_password = request.form['user_password']

    connection = get_flask_database_connection(app)
    repository = AccountRepository(connection)
    account = Account(None, username, email, user_password)
    repository.create(account)

    post = PostRepository(connection)
    posts = post.all()
        
    return render_template("posts.html", posts=posts)



@app.route('/login', methods=['GET'])
def get_login():
    return render_template("login.html")  


# @app.route('/login', methods=['POST'])
# def login_post():
#     email = request.form.get('email')
#     password = request.form.get('password')
#     # remember = True if request.form.get('remember') else False

#     user = User.query.filter_by(email=email).first()

#     # check if the user actually exists
#     # take the user-supplied password, hash it, and compare it to the hashed password in the database
#     # possibly change order of if statement
#     if not user or not check_password_hash(user.password, password):
#         flash('Please check your login details and try again.')
#         return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

#     # if the above check passes, then we know the user has the right credentials
#     return redirect(url_for('main.profile'))

@app.route('/newpost', methods=['GET', 'POST'])
def new_post():
    chars_left = 150
    if request.method == 'POST':
        username = request.form['username']
        content = request.form['textInput']

        connection = get_flask_database_connection(app)
        repository = PostRepository(connection)
        post = Post(None, content, username)
        repository.create(post)

        # Fetch all posts after creating the new post
        posts = repository.all()
        
        return render_template("posts.html", posts=posts)

    return render_template('new_post.html', chars_left=chars_left)


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
