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
                "discount_percentage": 25.0,
                "rent_price_before_discount": 199,
                "rent_price_after_discount": 150,
                "discount_price": 49,
                "damage_fine_percentage": 0,
                "overdue_fine_percentage": 0,
                "total_fine_percentage": 0,
                "fine_price": 0,
                "total_price": 150,
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
                "pledge_price": 822,
                "discount_percentage": 0,
                "rent_price_before_discount": 411,
                "rent_price_after_discount": 411,
                "discount_price": 0,
                "damage_fine_percentage": 0,
                "overdue_fine_percentage": 31,
                "total_fine_percentage": 31,
                "fine_price": 262,
                "total_price": 673,
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
                "pledge_price": 159,
                "discount_percentage": 10,
                "rent_price_before_discount": 79,
                "rent_price_after_discount": 71,
                "discount_price": 8,
                "damage_fine_percentage": 0,
                "overdue_fine_percentage": 0,
                "total_fine_percentage": 0,
                "fine_price": 0,
                "total_price": 71,
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
                "expected_rent_end_date": "2022-04-18",
                "rent_end_date": "2022-04-18",
                "pledge_price": 210,
                "discount_percentage": 0,
                "rent_price_before_discount": 105,
                "rent_price_after_discount": 105,
                "discount_price": 0,
                "damage_fine_percentage": 10,
                "overdue_fine_percentage": 0,
                "total_fine_percentage": 10,
                "fine_price": 21,
                "total_price": 126,
                "library_item": {
                    "id": 4,
                    "title": "Re-engineered demand-driven structure",
                    "author": "Bendix Dunsmuir",
                    "genre": "primis",
                },
            },
        ],
        "total_paid_rent": "326",
        "total_paid_pledge": "822",
        "total_paid_fine": "21",
        "total_paid": "1169",
        "total_unpaid_rent": "411",
        "total_unpaid_fine": "262",
        "total_unpaid": "673",
        "total_discount": "57",
    }
    return jsonify(financial_report_mock)
