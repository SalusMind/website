import uuid

from flask import Blueprint
from flask import session
from flask import redirect
from flask import jsonify
from flask import request

from common import models
from common import config


api = Blueprint('api', __name__)


#
# User
#

@api.route("/user/login", methods=['POST'])
@config.non_auth
def login():
    data = request.get_json()
    response = models.login(**data)
    if response['status']:
        session['user'] = response['message']
    return jsonify(response)


@api.route("/user/signup", methods=['POST'])
@config.non_auth
def signup():
    data = request.get_json()
    return jsonify(models.signup(**data))


@api.route("/user/forgot", methods=['POST'])
@config.non_auth
def forgot():
    data = request.get_json()
    return jsonify(models.forgot(**data))


@api.route('/user/confirm/<email>/<confirm_key>', methods=['GET'])
@config.non_auth
def confirm(email, confirm_key):
    confirmation = models.confirm(email, confirm_key)
    if confirmation['status']:
        return redirect('/login')
    else:
        return confirmation['message']


@api.route("/user/social", methods=['POST'])
@config.requires_auth
def connectAccount():
    data = request.get_json()
    data['email'] = session['user']['email']
    return jsonify(models.connect_account(**data))



#
# Organization
#

@api.route("/organization/<id>", methods=['GET'])
def get_organization():
    return True


@api.route("/organization/create", methods=['POST'])
def create_organization():
    return True

