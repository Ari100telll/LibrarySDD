from resources import db


class ReaderCategory(db.Model):
    __tablename__ = "reader_category"
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(30), unique=True)
    discount_percentage = db.Column(db.Numeric)

    @staticmethod
    def from_dict(body: dict):
        category = body.get("category", None)
        discount_percentage = body.get("discount_percentage", None)
        return ReaderCategory(
            category=category, discount_percentage=discount_percentage
        )

    def __repr__(self):
        return str(self.__dict__)
