import json

from flask import Blueprint

books_bp = Blueprint("books_blueprint", __name__, url_prefix="/books")


@books_bp.route("/", methods=["GET"])
def get_all_books():
    books = []
    return json.dumps(books)


@books_bp.route("/<int:book_id>", methods=["GET"])
def get_book(book_id: int):
    book = {}
    return json.dumps(book)


@books_bp.route("/", methods=["POST"])
def create_book():
    new_book = {}
    return json.dumps(new_book)


@books_bp.route("/<int:book_id>", methods=["PUT"])
def update_book(book_id: int):
    old_book = {}
    return json.dumps(old_book)


@books_bp.route("/<int:book_id>", methods=["DELETE"])
def delete_book(book_id: int):
    deleted_book = {}
    return json.dumps(deleted_book)
