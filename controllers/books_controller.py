from flask import Blueprint, jsonify, request

books_bp = Blueprint("books_blueprint", __name__, url_prefix="/books")


@books_bp.route("/", methods=["GET"])
def get_all_books():
    books = [
        {
            "id": 1,
            "pledge_price": 191,
            "quantity": 42,
            "title": "Synergized scalable help-desk",
            "author": "Yancy Chilles",
            "genre": "luctus",
        },
        {
            "id": 2,
            "pledge_price": 51,
            "quantity": 12,
            "title": "Front-line dedicated local area network",
            "author": "Nickola Batalle",
            "genre": "sagittis",
        },
        {
            "id": 3,
            "pledge_price": 59,
            "quantity": 37,
            "title": "Phased logistical emulation",
            "author": "Ritchie Saph",
            "genre": "nullam",
        },
        {
            "id": 4,
            "pledge_price": 398,
            "quantity": 9,
            "title": "Re-engineered demand-driven structure",
            "author": "Bendix Dunsmuir",
            "genre": "primis",
        },
        {
            "id": 5,
            "pledge_price": 397,
            "quantity": 84,
            "title": "Ergonomic empowering success",
            "author": "Drusy Spaduzza",
            "genre": "neque",
        },
        {
            "id": 6,
            "pledge_price": 612,
            "quantity": 73,
            "title": "Virtual local service-desk",
            "author": "Lorene Well",
            "genre": "sed",
        },
        {
            "id": 7,
            "pledge_price": 497,
            "quantity": 89,
            "title": "De-engineered context-sensitive installation",
            "author": "Esme Shurville",
            "genre": "id",
        },
        {
            "id": 8,
            "pledge_price": 592,
            "quantity": 65,
            "title": "Future-proofed high-level firmware",
            "author": "Damon Hover",
            "genre": "erat",
        },
        {
            "id": 9,
            "pledge_price": 432,
            "quantity": 71,
            "title": "Enterprise-wide fresh-thinking archive",
            "author": "Gwenette Gloy",
            "genre": "at",
        },
        {
            "id": 10,
            "pledge_price": 74,
            "quantity": 57,
            "title": "Automated fault-tolerant synergy",
            "author": "Gabriela Cuxon",
            "genre": "consequat",
        },
    ]
    return jsonify(books)


@books_bp.route("/<int:book_id>", methods=["GET"])
def get_book(book_id: int):
    book = {
        "id": book_id,
        "pledge_price": 867,
        "quantity": 32,
        "title": "Right-sized interactive open architecture",
        "author": "Willey Bricknell",
        "genre": "vitae",
    }
    return jsonify(book)


@books_bp.route("/", methods=["POST"])
def create_book():
    new_book = request.get_json()
    new_book["id"] = 123
    return jsonify(new_book)


@books_bp.route("/<int:book_id>", methods=["PUT"])
def update_book(book_id: int):
    old_book = {
        "id": book_id,
        "pledge_price": 969,
        "quantity": 39,
        "title": "Progressive fault-tolerant alliance",
        "author": "Trumann Gullberg",
        "genre": "ornare",
    }
    return jsonify(old_book)


@books_bp.route("/<int:book_id>", methods=["DELETE"])
def delete_book(book_id: int):
    deleted_book = {
        "id": book_id,
        "pledge_price": 889,
        "quantity": 48,
        "title": "Total mobile firmware",
        "author": "Winonah Szymanek",
        "genre": "morbi",
    }
    return jsonify(deleted_book)
