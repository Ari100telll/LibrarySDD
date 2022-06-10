from sqlalchemy import Column, Enum, Integer, String
from sqlalchemy.orm import relationship

import utils.db
from models.book_genre import BookGenre


class Book(utils.db.Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    author = Column(String(60))
    genre = Column(Enum(BookGenre))
    rent = relationship("Rent", backref="book")

    def __repr__(self):
        return str(self.__dict__)
