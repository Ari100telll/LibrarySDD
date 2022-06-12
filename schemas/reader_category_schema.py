from models.reader_category import ReaderCategory
from resources import ma


class ReaderCategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ReaderCategory


reader_category_schema = ReaderCategorySchema()
reader_categories_schema = ReaderCategorySchema(many=True)
