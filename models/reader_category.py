from sqlalchemy import Column, Integer, Numeric, String
from sqlalchemy.orm import relationship

import utils.db


class ReaderCategory(utils.db.Base):
    __tablename__ = "reader_category"
    id = Column(Integer, primary_key=True)
    category = Column(String(30))
    discount_percentage = Column(Numeric)
    users = relationship("User", backref="reader_category")

    def __repr__(self):
        return str(self.__dict__)
