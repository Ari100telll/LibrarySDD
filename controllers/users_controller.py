from http import HTTPStatus

from flask import Blueprint, jsonify, request, Response

from resources import db
from utils.create_entity import create_entity
from utils.delete_entity import delete_entity

from models.user import User
from schemas.user_schema import user_schema, users_schema

users_bp = Blueprint("users_blueprint", __name__, url_prefix="/users")


@users_bp.route("/", methods=["GET"])
def get_all_users():
    users = User.query.all()

    return users_schema.jsonify(users)


@users_bp.route("/<int:user_id>")
def get_user(user_id: int):
    single_user = User.query.get_or_404(user_id)

    return user_schema.jsonify(single_user)


@users_bp.route("/", methods=["POST"])
def create_user():
    body = request.get_json()

    return create_entity(body=body, model=User, unique_field='phone_number')


@users_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id: int):
    body = request.get_json()

    user_update_body = {
        "name": body.get("name", None),
        "surname": body.get("surname", None),
        "phone_number": body.get("phone_number", None),
        "address": body.get("address", None),
        "reader_category_id": body.get("reader_category_id", None)
    }

    User.query.filter_by(id=user_id).update(user_update_body)
    db.session.commit()

    return jsonify(user_update_body)


@users_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id: int):
    return delete_entity(model=User, entity_id=user_id)


@users_bp.route("/<int:user_id>/rents:summarize", methods=["GET"])
def get_user_financial_report(user_id: int):
    financial_report_mock = {
        "user_id:": user_id,
        "rents": [
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
        "total_discount_price": "57",
    }
    return jsonify(financial_report_mock)


@users_bp.route("/<int:user_id>/rents", methods=["GET"])
def get_user_rents(user_id: int):
    user_rents_mock = [
        {
            "id": 1,
            "user": {
                "id": user_id,
                "name": "Kuipers",
                "surname": "Alkyone",
                "phone_number": "+380(048)69-85-63",
                "address": "Ukraine, Chernigiv, Starobіlouska Vul., bld. 33, appt. 69",
                "category": {"category": "reader1", "discount_percentage": 20.0},
            },
            "rent_start_date": "2021-09-19 07:12:15",
            "expected_rent_end_date": "2021-10-05 20:18:46",
            "rent_end_date": "",
            "library_item": {
                "id": 1,
                "pledge_price": 191,
                "quantity": 42,
                "title": "Synergized scalable help-desk",
                "author": "Yancy Chilles",
                "genre": "luctus",
            },
            "rent_price": 697,
            "fine_price": 120,
            "damage_level": {
                "id": 1,
                "level": "level1",
                "finePercentage": 20.0,
            },
        },
        {
            "id": 2,
            "user": {
                "id": user_id,
                "name": "Kuipers",
                "surname": "Alkyone",
                "phone_number": "+380(048)69-85-63",
                "address": "Ukraine, Chernigiv, Starobіlouska Vul., bld. 33, appt. 69",
                "category": {"category": "reader1", "discount_percentage": 20.0},
            },
            "rent_start_date": "2021-07-17 19:36:37",
            "expected_rent_end_date": "2021-09-16 17:09:06",
            "rent_end_date": "",
            "library_item": {
                "id": 2,
                "pledge_price": 51,
                "quantity": 12,
                "title": "Front-line dedicated local area network",
                "author": "Nickola Batalle",
                "genre": "sagittis",
            },
            "rent_price": 822,
            "fine_price": 324,
            "damage_level": {
                "id": 2,
                "level": "level2",
                "finePercentage": 25.0,
            },
        },
        {
            "id": 3,
            "user": {
                "id": user_id,
                "name": "Kuipers",
                "surname": "Alkyone",
                "phone_number": "+380(048)69-85-63",
                "address": "Ukraine, Chernigiv, Starobіlouska Vul., bld. 33, appt. 69",
                "category": {"category": "reader1", "discount_percentage": 20.0},
            },
            "rent_start_date": "2021-10-29 00:32:46",
            "expected_rent_end_date": "2021-12-22 22:35:21",
            "rent_end_date": "",
            "library_item": {
                "id": 3,
                "pledge_price": 59,
                "quantity": 37,
                "title": "Phased logistical emulation",
                "author": "Ritchie Saph",
                "genre": "nullam",
            },
            "rent_price": 527,
            "fine_price": 0,
            "damage_level": {
                "id": 3,
                "level": "level3",
                "finePercentage": 15.0,
            },
        },
        {
            "id": 4,
            "user": {
                "id": user_id,
                "name": "Kuipers",
                "surname": "Alkyone",
                "phone_number": "+380(048)69-85-63",
                "address": "Ukraine, Chernigiv, Starobіlouska Vul., bld. 33, appt. 69",
                "category": {"category": "reader1", "discount_percentage": 20.0},
            },
            "rent_start_date": "2022-03-15 08:42:58",
            "expected_rent_end_date": "2022-05-18 12:17:33",
            "rent_end_date": "2022-03-23 00:51:16",
            "library_item": {
                "id": 4,
                "pledge_price": 398,
                "quantity": 9,
                "title": "Re-engineered demand-driven structure",
                "author": "Bendix Dunsmuir",
                "genre": "primis",
            },
            "rent_price": 342,
            "fine_price": 0,
            "damage_level": {
                "id": 4,
                "category": "level4",
                "finePercentage": 30.0,
            },
        },
        {
            "id": 5,
            "user": {
                "id": user_id,
                "name": "Kuipers",
                "surname": "Alkyone",
                "phone_number": "+380(048)69-85-63",
                "address": "Ukraine, Chernigiv, Starobіlouska Vul., bld. 33, appt. 69",
                "category": {"category": "reader1", "discount_percentage": 20.0},
            },
            "rent_start_date": "2022-01-17 13:23:07",
            "expected_rent_end_date": "2022-04-14 23:58:38",
            "rent_end_date": "2022-01-18 14:24:19",
            "library_item": {
                "id": 5,
                "pledge_price": 397,
                "quantity": 84,
                "title": "Ergonomic empowering success",
                "author": "Drusy Spaduzza",
                "genre": "neque",
            },
            "rent_price": 155,
            "fine_price": 0,
            "damage_level": {
                "id": 5,
                "level": "level5",
                "finePercentage": 45.0,
            },
        },
    ]
    return jsonify(user_rents_mock)


@users_bp.route("/<int:id>/rents:request", methods=["POST"])
def request_rent(user_id: int):
    rent_request = request.get_json()

    rent = rent_request["rent"]
    # payment_strategy = rent_request["payment_strategy"] just for example what body structure contains

    created_rent_mock = {
        "id": 100,
        "user": rent["user"],
        "rent_start_date": rent["rent_start_date"],
        "expected_rent_end_date": rent["expected_rent_end_date"],
        "rent_end_date": "",
        "library_item": rent["library_item"],
        "rent_price": 352,
        "fine_price": 0,
        "damage_level": "",
    }
    return jsonify(created_rent_mock)
