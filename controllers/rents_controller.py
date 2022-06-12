from flask import Blueprint, jsonify, request

from models.rent import Rent
from resources import db
from schemas.rent_schema import rent_schema, rents_schema
from services.reports.report_manager import ReportManager
from utils.create_entity import create_entity
from utils.delete_entity import delete_entity

rents_bp = Blueprint("rents_blueprint", __name__, url_prefix="/rents")


@rents_bp.route("/", methods=["GET"])
def get_all_rents():
    rents = Rent.query.all()

    return rents_schema.jsonify(rents)


@rents_bp.route("/<int:rent_id>", methods=["GET"])
def get_rent(rent_id: int):
    single_rent = Rent.query.get_or_404(rent_id)

    return rent_schema.jsonify(single_rent)


@rents_bp.route("/", methods=["POST"])
def create_rent():
    body = request.get_json()

    return create_entity(body=body, model=Rent, unique_field=None)


@rents_bp.route("/<int:rent_id>", methods=["PUT"])
def update_rent(rent_id: int):
    body = request.get_json()

    rent_update_body = {
        "library_user_id": body.get("library_user_id", None),
        "rent_start_date": body.get("rent_start_date", None),
        "expected_rent_end_date": body.get("expected_rent_end_date", None),
        "rent_end_date": body.get("rent_end_date", None),
        "library_item_id": body.get("library_item_id", None),
        "rent_price": body.get("rent_price", None),
        "fine_price": body.get("fine_price", None),
        "damage_level_id": body.get("damage_level_id", None),
    }

    Rent.query.filter_by(id=rent_id).update(rent_update_body)
    db.session.commit()

    return jsonify(rent_update_body)


@rents_bp.route("/<int:rent_id>", methods=["DELETE"])
def delete_rent(rent_id: int):
    return delete_entity(model=Rent, entity_id=rent_id)


@rents_bp.route("/summarize", methods=["GET"])
def get_library_financial_report():
    library_financial_report = ReportManager.get_library_financial_report()
    return jsonify(library_financial_report)


@rents_bp.route("/<int:id>:return", methods=["POST"])
def return_rent(rent_id: int):
    rent = request.get_json()
    updated_rent_mock = {
        "id": rent_id,
        "user": rent["user"],
        "rent_start_date": rent["rent_start_date"],
        "expected_rent_end_date": rent["expected_rent_end_date"],
        "rent_end_date": "2022-03-31 11:03:38",
        "library_item": rent["library_item"],
        "rent_price": rent["rent_price"],
        "fine_price": 91,
        "damage_level": {
            "id": 3,
            "level": "level5",
            "fine_percentage": 45.0,
        },
    }
    return jsonify(updated_rent_mock)
