from marshmallow_enum import EnumField
from marshmallow_sqlalchemy import auto_field

from models.book import Book
from models.book_genre import BookGenre
from resources import ma
from schemas.library_item_schema import LibraryItemSchema


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        include_relationships = True

    id = auto_field()
    library_item = ma.Nested(LibraryItemSchema(), exclude=["id", "book"])
    genre = EnumField(BookGenre)


book_schema = BookSchema()
books_schema = BookSchema(many=True)
