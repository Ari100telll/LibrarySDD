from http import HTTPStatus

from flask import Blueprint, Response, request

from schemas.book_schema import book_schema, books_schema
from services.factory.book_factory import BookFactory

books_bp = Blueprint("books_blueprint", __name__, url_prefix="/books")
book_factory = BookFactory()


@books_bp.route("/", methods=["GET"])
def get_all_books():
    books = book_factory.get_library_items()
    return books_schema.jsonify(books)


@books_bp.route("/<int:book_id>", methods=["GET"])
def get_book(book_id: int):
    book = book_factory.get_library_item_by(book_id)
    return book_schema.jsonify(book)


@books_bp.route("/", methods=["POST"])
def create_book():
    body = request.get_json()
    book = book_factory.create_library_item(body)
    return book_schema.jsonify(book)


@books_bp.route("/<int:book_id>", methods=["PUT"])
def update_book(book_id: int):
    body = request.get_json()
    book = book_factory.update_library_item(book_id, body)
    return book_schema.jsonify(book)


@books_bp.route("/<int:book_id>", methods=["DELETE"])
def delete_book(book_id: int):
    book_factory.delete_library_item(book_id)
    return Response(status=HTTPStatus.NO_CONTENT)
