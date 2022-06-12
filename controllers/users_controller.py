from http import HTTPStatus

from flask import Blueprint, Response, jsonify, request

from schemas.rent_schema import rents_schema
from services.reports.report_manager import ReportManager

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
    financial_report = ReportManager.get_user_financial_report(user_id)
    return jsonify(financial_report)


@users_bp.route("/<int:user_id>/rents", methods=["GET"])
def get_user_rents(user_id: int):
    user_rents = ReportManager.get_rents(user_id)
    return rents_schema.jsonify(user_rents)


@users_bp.route("/<int:user_id>/rents:request", methods=["POST"])
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
