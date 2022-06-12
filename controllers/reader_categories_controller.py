from http import HTTPStatus

from flask import Blueprint, jsonify, request, Response

from models.reader_category import ReaderCategory
from resources import db

from schemas.reader_category_schema import reader_categories_schema, reader_category_schema

reader_categories_bp = Blueprint(
    "reader_categories_blueprint", __name__, url_prefix="/reader_categories"
)


@reader_categories_bp.route("/", methods=["GET"])
def get_all_reader_categories():
    reader_categories = ReaderCategory.query.all()

    return reader_categories_schema.jsonify(reader_categories)


@reader_categories_bp.route("/<int:reader_category_id>")
def get_reader_category(reader_category_id: int):
    single_reader_category = ReaderCategory.query.get_or_404(reader_category_id)

    return reader_category_schema.jsonify(single_reader_category)


@reader_categories_bp.route("/", methods=["POST"])
def create_reader_category():
    body = request.get_json()
    category = body.get('category')
    reader_category_already_exists = ReaderCategory.query.filter_by(category=category).first()

    if reader_category_already_exists:
        return {'err': f'Category {category} already exists'}, 400

    try:
        new_reader_category = ReaderCategory.from_dict(body)
        db.session.add(new_reader_category)
        db.session.commit()
        return jsonify(body), 201

    except Exception as e:
        return str(e)


@reader_categories_bp.route("/<int:reader_category_id>", methods=["PUT"])
def update_reader_category(reader_category_id: int):
    body = request.get_json()

    reader_category_update_body = {
        "category": body.get("category", None),
        "discount_percentage": body.get("discount_percentage", None),
    }

    ReaderCategory.query.filter_by(id=reader_category_id).update(reader_category_update_body)
    db.session.commit()

    return jsonify(reader_category_update_body)


@reader_categories_bp.route("/<int:reader_category_id>", methods=["DELETE"])
def delete_reader_category(reader_category_id: int):
    reader_category = ReaderCategory.query.get_or_404(reader_category_id)

    db.session.delete(reader_category)
    db.session.commit()
    return Response(status=HTTPStatus.NO_CONTENT)
