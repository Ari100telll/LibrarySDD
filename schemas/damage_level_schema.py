from models.damage_level import DamageLevel
from resources import ma


class DamageLevelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DamageLevel


damage_level_schema = DamageLevelSchema()
damage_levels_schema = DamageLevelSchema(many=True)
