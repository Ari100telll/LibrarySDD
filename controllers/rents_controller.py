from http import HTTPStatus

from flask import Blueprint, jsonify, request, Response

from models.rent import Rent
from resources import db
from schemas.rent_schema import rent_schema, rents_schema
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
        "damage_level_id": body.get("damage_level_id", None)
    }

    Rent.query.filter_by(id=rent_id).update(rent_update_body)
    db.session.commit()

    return jsonify(rent_update_body)


@rents_bp.route("/<int:rent_id>", methods=["DELETE"])
def delete_rent(rent_id: int):
    return delete_entity(model=Rent, entity_id=rent_id)


@rents_bp.route(":summarize", methods=["GET"])
def get_library_financial_report():
    library_financial_report_mock = {
        "rents": [
            {
                "id": 1,
                "user": {
                    "id": 1,
                    "name": "Kuipers",
                    "surname": "Alkyone",
                    "phone_number": "+380(048)69-85-63",
                    "address": "Ukraine, Chernigiv, Starobіlouska Vul., bld. 33, appt. 69",
                    "category": "reader1",
                },
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
                    "quantity": 9,
                    "title": "Re-engineered demand-driven structure",
                    "author": "Bendix Dunsmuir",
                    "genre": "primis",
                },
            },
            {
                "id": 2,
                "user": {
                    "id": 2,
                    "name": "Micaela",
                    "surname": "Stack",
                    "phone_number": "+380(0542)34-17-38",
                    "address": "Ukraine, Rivne, Shevchenko Vul., bld. 21, appt. 32",
                    "category": "reader2",
                },
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
                    "quantity": 2,
                    "title": "Front-line dedicated local area network",
                    "author": "Nickola Batalle",
                    "genre": "sagittis",
                },
            },
            {
                "id": 3,
                "user": {
                    "id": 3,
                    "name": "Hanifa",
                    "surname": "Nicolai",
                    "phone_number": "+380(0692)49-94-67",
                    "address": "Ukraine, Priluki, Polova Vul., bld. 100, appt. 54",
                    "category": {"category": "reader3", "discount_percentage": 15.0},
                },
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
                    "quantity": 4,
                    "title": "Phased logistical emulation",
                    "author": "Ritchie Saph",
                    "genre": "nullam",
                },
            },
            {
                "id": 4,
                "user": {
                    "id": 4,
                    "name": "Alden",
                    "surname": "Gunnarr",
                    "phone_number": "+380(0652)22-17-09",
                    "address": "Ukraine, Kharkiv, Odeska Vul., bld. 2, appt. 26",
                    "category": {"category": "reader4", "discount_percentage": 30.0},
                },
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
                    "quantity": 11,
                    "title": "Re-engineered demand-driven structure",
                    "author": "Bendix Dunsmuir",
                    "genre": "primis",
                },
            },
        ],
        "total_received_rent_price": "326",
        "total_received_pledge_price": "822",
        "total_received_fine_price": "21",
        "total_received": "1169",
        "total_pending_rent_price": "411",
        "total_pending_fine_price": "262",
        "total_pending": "673",
        "total_discount_price": "57",
    }
    return jsonify(library_financial_report_mock)


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
