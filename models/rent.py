from resources import db


class Rent(db.Model):
    __tablename__ = "rent"
    id = db.Column(db.Integer, primary_key=True)
    library_user_id = db.Column(db.Integer, db.ForeignKey("library_user.id"))
    library_user = db.relationship("User", backref="rents")
    rent_start_date = db.Column(db.Date)
    expected_rent_end_date = db.Column(db.Date)
    rent_end_date = db.Column(db.Date)
    library_item_id = db.Column(db.Integer, db.ForeignKey("library_item.id"))
    library_item = db.relationship("LibraryItem", backref="rents")
    rent_price = db.Column(db.Numeric)
    fine_price = db.Column(db.Numeric)
    damage_level_id = db.Column(db.Integer, db.ForeignKey("damage_level.id"))
    damage_level = db.relationship("DamageLevel", backref="rents")

    def __repr__(self):
        return str(self.__dict__)
