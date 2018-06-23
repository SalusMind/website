import os

from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import session

from authlib.flask.client import OAuth

from common import config
from api.rest import api


app = Flask(__name__)
app.secret_key = config.SECRET_KEY
app.register_blueprint(api, url_prefix='/api')

oauth = OAuth(app)
auth0 = oauth.register(
    'auth0',
    client_id='lCFqlmkmn-CiumefwhbKS5x5bM7GmbyT',
    client_secret='vGgiywHmRUcLY4j2fQDXWHr0HzItvTS8BXLX1kS1Fdm8LJqR74N4Fvs_IQwLi0nW',
    api_base_url='https://salusmind.auth0.com',
    access_token_url='https://salusmind.auth0.com/oauth/token',
    authorize_url='https://salusmind.auth0.com/authorize',
    client_kwargs={
        'scope': 'openid profile',
    }
)


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
    print(session['profile'])
    return render_template('profile.html', profile=session['profile'])


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
    config.g.auth0 = auth0

