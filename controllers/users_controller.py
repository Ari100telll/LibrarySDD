import json

from flask import Blueprint

users_bp = Blueprint("users_blueprint", __name__, url_prefix="/users")


@users_bp.route("/", methods=["GET"])
def get_all_users():
    users_mock = [
        {
            "id": 1,
            "name": "Kuipers",
            "surname": "Alkyone",
            "phoneNumber": "+380(048)69-85-63",
            "address": "Ukraine, Chernigiv, Starobіlouska Vul., bld. 33, appt. 69",
            "category": {"category": "reader1", "discountPercentage": 20.0},
        },
        {
            "id": 2,
            "name": "Micaela",
            "surname": "Stack",
            "phoneNumber": "+380(0542)34-17-38",
            "address": "Ukraine, Rivne, Shevchenko Vul., bld. 21, appt. 32",
            "category": {"category": "reader2", "discountPercentage": 25.0},
        },
        {
            "id": 3,
            "name": "Hanifa",
            "surname": "Nicolai",
            "phoneNumber": "+380(0692)49-94-67",
            "address": "Ukraine, Priluki, Polova Vul., bld. 100, appt. 54",
            "category": {"category": "reader3", "discountPercentage": 15.0},
        },
        {
            "id": 4,
            "name": "Alden",
            "surname": "Gunnarr",
            "phoneNumber": "+380(0652)22-17-09",
            "address": "Ukraine, Kharkiv, Odeska Vul., bld. 2, appt. 26",
            "category": {"category": "reader4", "discountPercentage": 30.0},
        },
        {
            "id": 5,
            "name": "Zaman",
            "surname": "Malloye",
            "phoneNumber": "+380(06562)4-00-63",
            "address": "Ukraine, Lviv, Naukova Vul., bld. 13, appt. 20",
            "category": {"category": "reader5", "discountPercentage": 25.0},
        },
    ]
    return json.dumps(users_mock)


@users_bp.route("/<int:id>")
def get_user(user_id: int):
    user_mock = {
        "id": user_id,
        "name": "Kuipers",
        "surname": "Alkyone",
        "phoneNumber": "+380(048)69-85-63",
        "address": "Ukraine, Chernigiv, Starobіlouska Vul., bld. 33, appt. 69",
        "category": {"category": "reader1", "discountPercentage": 20.0},
    }

    return json.dumps(user_mock)
