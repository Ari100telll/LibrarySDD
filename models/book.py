from sqlalchemy import Column, Enum, Integer, String

import utils.db
from models.book_genre import BookGenre


class Book(utils.db.Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    author = Column(String(60))
    genre = Column(Enum(BookGenre))

    def __repr__(self):
        return str(self.__dict__)
