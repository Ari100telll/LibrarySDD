from flask import Blueprint, jsonify, request

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
    return jsonify(users_mock)


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

    return jsonify(user_mock)


@users_bp.route("/", methods=["POST"])
def create_user():
    new_user = request.get_json()
    new_user.id = 6
    return jsonify(new_user)


@users_bp.route("/<int:id>", methods=["PUT"])
def update_user(user_id: int):
    old_user_mock = {
        "id": user_id,
        "name": "Kuipers",
        "surname": "Alkyone",
        "phoneNumber": "+380(048)69-85-63",
        "address": "Ukraine, Chernigiv, Starobіlouska Vul., bld. 33, appt. 69",
        "category": {"category": "reader1", "discountPercentage": 20.0},
    }

    return jsonify(old_user_mock)


@users_bp.route("/<int:id>", methods=["DELETE"])
def delete_user(user_id: int):
    deleted_user_mock = {
        "id": user_id,
        "name": "Kuipers",
        "surname": "Alkyone",
        "phoneNumber": "+380(048)69-85-63",
        "address": "Ukraine, Chernigiv, Starobіlouska Vul., bld. 33, appt. 69",
        "category": {"category": "reader1", "discountPercentage": 20.0},
    }

    return jsonify(deleted_user_mock)


@users_bp.route("/<int:id>/rents:summarize", methods=["GET"])
def get_user_financial_report(user_id: int):
    financial_report_mock = {
        "user_id:": user_id,
        "records": [
            {
                "id": 1,
                "rent_start_date": "2022-03-15",
                "expected_rent_end_date": "2022-05-18",
                "rent_end_date": "2022-03-23",
                "pledge_price": 398,
                "rent_price": 342,
                "fine_price": 0,
                "discount_percentage": 25.0,
                "fine_percentage": 0,
                "library_item": {
                    "id": 4,
                    "title": "Re-engineered demand-driven structure",
                    "author": "Bendix Dunsmuir",
                    "genre": "primis",
                },
            },
            {
                "id": 2,
                "rent_start_date": "2021-07-17",
                "expected_rent_end_date": "2021-09-16",
                "rent_end_date": "",
                "pledge_price": 51,
                "rent_price": 822,
                "fine_price": 324,
                "discount_percentage": 0,
                "fine_percentage": 20,
                "library_item": {
                    "id": 2,
                    "title": "Front-line dedicated local area network",
                    "author": "Nickola Batalle",
                    "genre": "sagittis",
                },
            },
            {
                "id": 3,
                "rent_start_date": "2022-01-12",
                "expected_rent_end_date": "2021-02-12",
                "rent_end_date": "2021-02-12",
                "pledge_price": 59,
                "rent_price": 25,
                "fine_price": 0,
                "discount_percentage": 10,
                "fine_percentage": 0,
                "library_item": {
                    "id": 3,
                    "title": "Phased logistical emulation",
                    "author": "Ritchie Saph",
                    "genre": "nullam",
                },
            },
            {
                "id": 4,
                "rent_start_date": "2022-03-18",
                "expected_rent_end_date": "2021-04-18",
                "rent_end_date": "",
                "pledge_price": 398,
                "rent_price": 150,
                "fine_price": 20,
                "discount_percentage": 0,
                "fine_percentage": 2,
                "library_item": {
                    "id": 4,
                    "title": "Re-engineered demand-driven structure",
                    "author": "Bendix Dunsmuir",
                    "genre": "primis",
                },
            },
        ],
    }
    return jsonify(financial_report_mock)
