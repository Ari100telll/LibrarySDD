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

    @staticmethod
    def from_dict(body: dict):
        title = body.get("title", None)
        author = body.get("author", None)
        genre = (body.get("genre", None) or "").upper()
        return Book(title=title, author=author, genre=genre)
