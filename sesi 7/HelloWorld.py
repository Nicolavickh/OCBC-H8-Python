from flask import Flask
from markupsafe import escape
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):    
    return render_template('hello.html', name=name)

@app.route('/')
def index():
    return 'Index Page'

# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"

@app.route('/user/<username>')
def show_user_profile(username):   
    return f'User {escape(username)}'
    
@app.route('/post/<int:post_id>')
def show_post(post_id):   
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'

@app.route('/login', methods=['GET', 'POST'])
def login():    
    if request.method == 'POST':        
        return do_the_login()    
    else:        
        return show_the_login_form()

if __name__ == '__main__':
    app.run(debug=True)