from http import HTTPStatus

from flask import Blueprint, Response, jsonify, request

from schemas.rent_schema import rents_schema
from services.report_manager import ReportManager

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
    user_rents = ReportManager.get_rents(user_id)
    return rents_schema.jsonify(user_rents)


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
