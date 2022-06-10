from sqlalchemy import Column, Date, ForeignKey, Integer, Numeric

import utils.db


class Rent(utils.db.Base):
    __tablename__ = "rent"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("library_user.id"))
    rent_start_date = Column(Date)
    expected_rent_end_date = Column(Date)
    rent_end_date = Column(Date)
    book_id = Column(Integer, ForeignKey("book.id"))
    rent_price = Column(Numeric)
    fine_price = Column(Numeric)
    damage_level_id = Column(Integer, ForeignKey("damage_level.id"))

    def __repr__(self):
        return str(self.__dict__)
