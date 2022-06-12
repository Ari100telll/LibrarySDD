from http import HTTPStatus

from flask import Blueprint, jsonify, request

from models.damage_level import DamageLevel
from resources import db

from utils.create_entity import create_entity
from utils.delete_entity import delete_entity

from schemas.damage_level_schema import damage_levels_schema, damage_level_schema

damage_levels_bp = Blueprint(
    "damage_levels_blueprint", __name__, url_prefix="/damage_levels"
)


@damage_levels_bp.route("/", methods=["GET"])
def get_all_damage_levels():
    damage_levels = DamageLevel.query.all()

    return damage_levels_schema.jsonify(damage_levels)


@damage_levels_bp.route("/<int:damage_level_id>")
def get_damage_level(damage_level_id: int):
    single_damage_level = DamageLevel.query.get_or_404(damage_level_id)

    return damage_level_schema.jsonify(single_damage_level)


@damage_levels_bp.route("/", methods=["POST"])
def create_damage_level():
    body = request.get_json()

    return create_entity(body=body, model=DamageLevel, unique_field='level')


@damage_levels_bp.route("/<int:damage_level_id>", methods=["PUT"])
def update_damage_level(damage_level_id: int):
    body = request.get_json()

    damage_level_update_body = {
        "level": body.get("level", None),
        "fine_percentage": body.get("fine_percentage", None),
    }

    DamageLevel.query.filter_by(id=damage_level_id).update(damage_level_update_body)
    db.session.commit()

    return jsonify(damage_level_update_body)


@damage_levels_bp.route("/<int:damage_level_id>", methods=["DELETE"])
def delete_damage_level(damage_level_id: int):
    return delete_entity(model=DamageLevel, entity_id=damage_level_id)
