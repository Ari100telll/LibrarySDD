from resources import db


class Rent(db.Model):
    __tablename__ = "rent"
    id = db.Column(db.Integer, primary_key=True)
    library_user_id = db.Column(db.Integer, db.ForeignKey("library_user.id"))
    rent_start_date = db.Column(db.Date)
    expected_rent_end_date = db.Column(db.Date)
    rent_end_date = db.Column(db.Date)
    library_item_id = db.Column(db.Integer, db.ForeignKey("library_item.id"))
    library_item = db.relationship("LibraryItem", backref="rents")
    rent_price = db.Column(db.Numeric)
    fine_price = db.Column(db.Numeric)
    damage_level_id = db.Column(db.Integer, db.ForeignKey("damage_level.id"))
    damage_level = db.relationship("DamageLevel", backref="rents")

    @staticmethod
    def from_dict(body: dict):
        library_user_id = body.get("library_user_id", None)
        rent_start_date = body.get("rent_start_date", None)
        expected_rent_end_date = body.get("expected_rent_end_date", None)
        rent_end_date = body.get("rent_end_date", None)
        library_item_id = body.get("library_item_id", None)
        rent_price = body.get("rent_price", None)
        fine_price = body.get("fine_price", None)
        damage_level_id = body.get("damage_level_id", None)

        return Rent(library_user_id=library_user_id, rent_start_date=rent_start_date,
                    expected_rent_end_date=expected_rent_end_date, rent_end_date=rent_end_date,
                    library_item_id=library_item_id, rent_price=rent_price, fine_price=fine_price,
                    damage_level_id=damage_level_id)

    def __repr__(self):
        return str(self.__dict__)
