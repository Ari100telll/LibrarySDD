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

    def __repr__(self):
        return str(self.__dict__)
