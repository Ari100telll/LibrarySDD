from models.book_genre import BookGenre
from resources import db


class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, db.ForeignKey("library_item.id"), primary_key=True)
    library_item = db.relationship(
        "LibraryItem", backref=db.backref("book", uselist=False, cascade="all,delete")
    )
    title = db.Column(db.String(50), unique=True)
    author = db.Column(db.String(60))
    genre = db.Column(db.Enum(BookGenre))

    def __repr__(self):
        return str(self.__dict__)
