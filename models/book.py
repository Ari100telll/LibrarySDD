from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

import utils.db
from models.book_genre import BookGenre


class Book(utils.db.Base):
    __tablename__ = "book"
    id = Column(Integer, ForeignKey("library_item.id"), primary_key=True)
    library_item = relationship("LibraryItem", backref=backref("book", uselist=False))
    title = Column(String(50))
    author = Column(String(60))
    genre = Column(Enum(BookGenre))

    def __repr__(self):
        return str(self.__dict__)
