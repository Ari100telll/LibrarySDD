from flask import Blueprint, jsonify, request

rents_bp = Blueprint("rents_blueprint", __name__, url_prefix="/rents")


@rents_bp.route("/", methods=["GET"])
def get_all_rents():
    rents = []
    return jsonify(rents)


@rents_bp.route("/<int:rent_id>", methods=["GET"])
def get_rent(rent_id: int):
    rent = {}
    return jsonify(rent)


@rents_bp.route("/", methods=["POST"])
def create_rent():
    new_rent = request.get_json()
    new_rent["id"] = 123
    return jsonify(new_rent)


@rents_bp.route("/<int:rent_id>", methods=["PUT"])
def update_rent(rent_id: int):
    old_rent = {}
    return jsonify(old_rent)


@rents_bp.route("/<int:rent_id>", methods=["DELETE"])
def delete_rent(rent_id: int):
    deleted_rent = {}
    return jsonify(deleted_rent)
