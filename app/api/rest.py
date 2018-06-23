import uuid

from flask import Blueprint
from flask import session
from flask import redirect
from flask import jsonify

from common import models
from common import config


api = Blueprint('api', __name__)


#
# User
#

@api.route("/auth")
def authenticate():
    config.g.auth0.authorize_access_token()
    resp = config.g.auth0.get('userinfo')
    print(resp.json())
    return redirect('/profile')



@api.route("/user/login", methods=['POST'])
def login():
    data = request.get_json()
    return jsonify(models.login(**data))


@api.route("/user/signup", methods=['POST'])
def signup():
    data = request.get_json()
    return jsonify(models.signup(**data))


@api.route("/user/forgot", methods=['POST'])
def forgot():
    data = request.get_json()
    return jsonify(models.forgot(**data))


#
# Organization
#

@api.route("/organization/<id>", methods=['GET'])
def get_organization():
    return True


@api.route("/organization/create", methods=['POST'])
def create_organization():
    return True

