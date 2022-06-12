from typing import List

from models.book import Book
from models.library_item import LibraryItem
from resources import db
from services.factory.library_item_factory import LibraryItemFactory


class BookFactory(LibraryItemFactory):
    def get_library_item_by(self, item_id: int) -> LibraryItem:
        return Book.query.get_or_404(item_id)

    def get_library_items(self) -> List[LibraryItem]:
        return Book.query.all()

    def delete_library_item(self, item_id: int) -> None:
        library_item = LibraryItem.query.get_or_404(item_id)

        db.session.delete(library_item)
        db.session.commit()

    def update_library_item(self, item_id: int, body: dict) -> LibraryItem:
        library_item_update_body = {
            "pledge_price": body.get("pledge_price", None),
            "quantity": body.get("quantity", None),
        }
        book_update_body = {
            "author": body.get("author", None),
            "title": body.get("title", None),
            "genre": body.get("genre", "").upper(),
        }

        Book.query.filter_by(id=item_id).update(book_update_body)
        LibraryItem.query.filter_by(id=item_id).update(library_item_update_body)

        db.session.commit()

        return self.get_library_item_by(item_id)

    def create_library_item(self, body: dict) -> LibraryItem:
        book = Book.from_dict(body)
        library_item = LibraryItem.from_dict(body)

        library_item.book = book

        db.session.add(library_item)
        db.session.commit()

        return book
