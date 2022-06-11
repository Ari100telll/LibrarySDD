from sqlalchemy import Column, Integer, Numeric

import utils.db


class LibraryItem(utils.db.Base):
    __tablename__ = "library_item"
    id = Column(Integer, primary_key=True)
    pledgePrice = Column(Numeric)
    quantity = Column(Integer)

    def __repr__(self):
        return str(self.__dict__)
