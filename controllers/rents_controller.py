from datetime import datetime

from flask import Blueprint, jsonify, request

from models.library_item import LibraryItem
from models.rent import Rent
from models.user import User
from resources import db
from schemas.rent_schema import rent_schema, rents_schema
from services.library_manager.library_manager import LibraryManager
from services.payment.bank_account_payment_strategy import BankAccountPaymentStrategy
from services.payment.card_payment_strategy import CardPaymentStrategy
from services.reports.report_manager import ReportManager
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
    payment_type = body.get("payment_strategy")
    if payment_type == "card":
        payment_strategy = CardPaymentStrategy()
    else:
        payment_strategy = BankAccountPaymentStrategy()

    rent_library_body = dict(
        library_item=LibraryItem.query.get(body.get("library_item_id")),
        user=User.query.filter_by(phone_number=body.get("phone_number")).first(),
        expected_rent_end_date=datetime.strptime(
            body.get("expected_rent_end_date"), "%Y-%m-%d"
        ),
        payment_strategy=payment_strategy,
    )

    rent = LibraryManager().rent_library_item(**rent_library_body)
    return rent_schema.jsonify(rent)


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


@rents_bp.route("/<int:rent_id>:return", methods=["POST"])
def return_rent(rent_id: int):
    rent_request = request.get_json()
    rent = Rent.query.get(rent_id)

    rent = LibraryManager().return_library_item(
        rent=rent, payment_type=rent_request.get("payment_type")
    )
    return rent_schema.jsonify(rent)
