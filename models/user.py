from resources import db


class User(db.Model):
    __tablename__ = "library_user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    phone_number = db.Column(db.String(13), unique=True)
    address = db.Column(db.String(40))
    reader_category_id = db.Column(db.Integer, db.ForeignKey("reader_category.id"))
    reader_category = db.relationship("ReaderCategory", backref="users")

    @staticmethod
    def from_dict(body: dict):
        name = body.get("name", None)
        surname = body.get("surname", None)
        phone_number = body.get("phone_number", None)
        address = body.get("address", None)
        reader_category_id = body.get("reader_category_id", None)
        return User(name=name, surname=surname, phone_number=phone_number, address=address,
                    reader_category_id=reader_category_id)

    def __repr__(self):
        return str(self.__dict__)
