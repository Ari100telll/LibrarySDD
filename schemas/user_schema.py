from models.user import User
from resources import ma
from schemas.reader_category_schema import ReaderCategorySchema


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True

    reader_category = ma.Nested(ReaderCategorySchema())


user_schema = UserSchema()
users_schema = UserSchema(many=True)
