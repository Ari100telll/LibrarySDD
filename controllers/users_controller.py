from datetime import datetime

from flask import Blueprint, jsonify, request

from models.library_item import LibraryItem
from models.user import User
from resources import db
from schemas.rent_schema import rent_schema, rents_schema
from schemas.user_schema import user_schema, users_schema
from services.library_manager.library_manager import LibraryManager
from services.reports.report_manager import ReportManager
from utils.create_entity import create_entity
from utils.delete_entity import delete_entity

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

    return create_entity(body=body, model=User, unique_field="phone_number")


@users_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id: int):
    body = request.get_json()

    user_update_body = {
        "name": body.get("name", None),
        "surname": body.get("surname", None),
        "phone_number": body.get("phone_number", None),
        "address": body.get("address", None),
        "reader_category_id": body.get("reader_category_id", None),
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

    rent_library_body = dict(
        library_item=LibraryItem.query.get(rent_request.get("library_item_id")),
        user=User.query.get(user_id),
        expected_rent_end_date=datetime.strptime(
            rent_request.get("expected_rent_end_date"), "%Y-%m-%d"
        ),
        payment_type=rent_request.get("payment_type"),
    )

    rent = LibraryManager().rent_library_item(**rent_library_body)
    return rent_schema.jsonify(rent)
