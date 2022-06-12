from enum import Enum

from resources import db


class DamageLevelValues(Enum):
    DESTROYED = "DESTROYED"
    MAJOR = "MAJOR"
    MINOR = "MINOR"
    AFFECTED = "AFFECTED"
    INACCESSIBLE = "INACCESSIBLE"


class DamageLevel(db.Model):
    __tablename__ = "damage_level"
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(30), unique=True)
    fine_percentage = db.Column(db.Numeric)

    def __repr__(self):
        return str(self.__dict__)
