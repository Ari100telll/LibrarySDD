from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

import utils.db


class User(utils.db.Base):
    __tablename__ = "library_user"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    surname = Column(String(50))
    phone_number = Column(String(13))
    address = Column(String(40))
    reader_category_id = Column(Integer, ForeignKey("reader_category.id"))
    reader_category = relationship("ReaderCategory", backref="users")
    rents = relationship("Rent", backref="user")

    def __repr__(self):
        return str(self.__dict__)
