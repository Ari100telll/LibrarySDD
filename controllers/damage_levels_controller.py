from flask import Blueprint, jsonify, request

damage_levels_bp = Blueprint(
    "damage_levels_blueprint", __name__, url_prefix="/damage_levels"
)


@damage_levels_bp.route("/", methods=["GET"])
def get_all_damage_levels():
    damage_levels_mock = [
        {
            "id": 1,
            "level": "level1",
            "finePercentage": 20.0,
        },
        {
            "id": 2,
            "level": "level2",
            "finePercentage": 25.0,
        },
        {
            "id": 3,
            "level": "level3",
            "finePercentage": 15.0,
        },
        {
            "id": 4,
            "category": "level4",
            "finePercentage": 30.0,
        },
        {
            "id": 5,
            "level": "level5",
            "finePercentage": 45.0,
        },
    ]
    return jsonify(damage_levels_mock)


@damage_levels_bp.route("/<int:id>")
def get_damage_level(damage_level_id: int):
    damage_level_mock = {
        "id": damage_level_id,
        "level": "level5",
        "finePercentage": 45.0,
    }

    return jsonify(damage_level_mock)


@damage_levels_bp.route("/", methods=["POST"])
def create_damage_level():
    new_damage_level = request.get_json()
    new_damage_level.id = 6
    return jsonify(new_damage_level)


@damage_levels_bp.route("/<int:id>", methods=["PUT"])
def update_damage_level(damage_level_id: int):
    old_damage_level_mock = {
        "id": damage_level_id,
        "level": "level5",
        "finePercentage": 45.0,
    }

    return jsonify(old_damage_level_mock)


@damage_levels_bp.route("/<int:id>", methods=["DELETE"])
def delete_damage_level(damage_level_id: int):
    deleted_damage_level_mock = {
        "id": damage_level_id,
        "level": "level5",
        "finePercentage": 45.0,
    }

    return jsonify(deleted_damage_level_mock)
