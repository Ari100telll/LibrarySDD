from models.rent import Rent
from resources import ma
from schemas.damage_level_schema import DamageLevelSchema
from schemas.library_item_schema import LibraryItemSchema
from schemas.user_schema import UserSchema


class RentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Rent
        include_relationships = True

    library_user = ma.Nested(UserSchema())
    library_item = ma.Nested(LibraryItemSchema())
    damage_level = ma.Nested(DamageLevelSchema())


rent_schema = RentSchema()
rents_schema = RentSchema(many=True)
