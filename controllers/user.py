import json

from flask import Blueprint

users_bp = Blueprint('users_blueprint', __name__, url_prefix="/users")


@users_bp.route("/", methods=['GET'])
def users():
    users = [{"id": 1, "name": "Kuipers", "surname": "Alkyone", "phoneNumber": "+380(048)69-85-63",
              "address": "Ukraine, Chernigiv, Starobіlouska Vul., bld. 33, appt. 69",
              "category": {"category": "reader", "discountPercentage": 0.2}}]
    return json.dumps(users)
