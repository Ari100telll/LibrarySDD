from sqlalchemy import Column, Integer, Numeric, String

import utils.db


class ReaderCategory(utils.db.Base):
    __tablename__ = "reader_category"
    id = Column(Integer, primary_key=True)
    category = Column(String(30))
    discount_percentage = Column(Numeric)

    def __repr__(self):
        return str(self.__dict__)
