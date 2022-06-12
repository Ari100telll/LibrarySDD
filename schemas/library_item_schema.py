from models.library_item import LibraryItem
from resources import ma


class LibraryItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LibraryItem
        include_relationships = True

    book = ma.Nested("BookSchema", exclude=["library_item", "id"])


library_item_schema = LibraryItemSchema()
library_items_schema = LibraryItemSchema(many=True)
