from flask import Blueprint

test_bp = Blueprint('test_blueprint', __name__, url_prefix="/test")


@test_bp.route("/", methods=['GET', 'POST'])
def ping():
    """Function which is triggered in flask app"""
    return "pong"
