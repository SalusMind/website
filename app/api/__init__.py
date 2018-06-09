from flask import Blueprint

api = Blueprint('api', __name__)


#
# User
#

@api.route("/user/login", methods=['POST'])
def login():
    return True


@api.route("/user/signup", methods=['POST'])
def signup():
    return True


@api.route("/user/forgot", methods=['POST'])
def forgot():
    return True


#
# Organization
#

@api.route("/organization/<id>", methods=['GET'])
def get_organization():
    return True


@api.route("/organization/create", methods=['POST'])
def create_organization():
    return True
