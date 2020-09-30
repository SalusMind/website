import os

from flask import Flask,render_template,session,redirect,url_for

from flask_bcrypt import Bcrypt

from common import config
from api.rest import api


app = Flask(__name__)
app.secret_key = config.SECRET_KEY
app.register_blueprint(api, url_prefix='/api')

bcrypt = Bcrypt(app)


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.route("/")
@config.non_auth
def home():
    return render_template('index.html')


@app.route('/login')
@config.non_auth
def login():
    return render_template('login.html')


@app.route('/signup')
@config.non_auth
def signup():
    return render_template('signup.html')


@app.route('/forgot')
@config.non_auth
def forgot():
    return render_template('forgot.html')


@app.route('/profile')
@config.requires_auth
def profile():
    return render_template('profile.html', user=session['user'])


@app.route('/signout')
@config.requires_auth
def signout():
    session.clear()
    return redirect('/')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


@app.before_request
def before_request():
    config.g.bcrypt = bcrypt

#  help in Running at localhost and wouldn't affect aws hosting
if __name__ == "__main__":
    app.run(debug=True)
