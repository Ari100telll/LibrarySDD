from resources import db


class DamageLevel(db.Model):
    __tablename__ = "damage_level"
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(30), unique=True)
    fine_percentage = db.Column(db.Numeric)

    @staticmethod
    def from_dict(body: dict):
        level = body.get("level", None)
        fine_percentage = body.get("fine_percentage", None)
        return DamageLevel(level=level, fine_percentage=fine_percentage)

    def __repr__(self):
        return str(self.__dict__)
