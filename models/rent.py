from sqlalchemy import Column, Date, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship

import utils.db


class Rent(utils.db.Base):
    __tablename__ = "rent"
    id = Column(Integer, primary_key=True)
    library_user_id = Column(Integer, ForeignKey("library_user.id"))
    library_user = relationship("User", backref="rents")
    rent_start_date = Column(Date)
    expected_rent_end_date = Column(Date)
    rent_end_date = Column(Date)
    book_id = Column(Integer, ForeignKey("book.id"))
    book = relationship("Book", backref="rents")
    rent_price = Column(Numeric)
    fine_price = Column(Numeric)
    damage_level_id = Column(Integer, ForeignKey("damage_level.id"))
    damage_level = relationship("DamageLevel", backref="rents")

    def __repr__(self):
        return str(self.__dict__)
