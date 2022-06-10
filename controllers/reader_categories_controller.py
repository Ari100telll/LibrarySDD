from http import HTTPStatus

from flask import Blueprint, jsonify, request, Response

reader_categories_bp = Blueprint(
    "reader_categories_blueprint", __name__, url_prefix="/reader_categories"
)


@reader_categories_bp.route("/", methods=["GET"])
def get_all_reader_categories():
    reader_categories_mock = [
        {
            "id": 1,
            "category": "reader1",
            "discount_percentage": 20.0,
        },
        {
            "id": 2,
            "category": "reader2",
            "discount_percentage": 25.0,
        },
        {
            "id": 3,
            "category": "reader3",
            "discount_percentage": 15.0,
        },
        {
            "id": 4,
            "category": "reader4",
            "discount_percentage": 30.0,
        },
        {
            "id": 5,
            "category": "reader5",
            "discount_percentage": 45.0,
        },
    ]
    return jsonify(reader_categories_mock)


@reader_categories_bp.route("/<int:id>")
def get_reader_category(reader_category_id: int):
    reader_category_mock = {
        "id": reader_category_id,
        "category": "reader5",
        "discount_percentage": 45.0,
    }

    return jsonify(reader_category_mock)


@reader_categories_bp.route("/", methods=["POST"])
def create_reader_category():
    new_reader_category = request.get_json()
    new_reader_category.id = 6
    return jsonify(new_reader_category)


@reader_categories_bp.route("/<int:id>", methods=["PUT"])
def update_reader_category(reader_category_id: int):
    updated_reader_category = request.get_json()
    updated_reader_category["id"] = reader_category_id
    return jsonify(updated_reader_category)


@reader_categories_bp.route("/<int:id>", methods=["DELETE"])
def delete_reader_category(reader_category_id: int):
    return Response(status=HTTPStatus.NO_CONTENT)
