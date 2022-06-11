from sqlalchemy import Column, Integer, Numeric

import utils.db
from utils.helpers import percentage_from


class LibraryItem(utils.db.Base):
    __tablename__ = "library_item"
    id = Column(Integer, primary_key=True)
    pledgePrice = Column(Numeric)
    quantity = Column(Integer)

    def __repr__(self):
        return str(self.__dict__)

    def calculate_rent_price_per_day(self) -> float:
        result = round(self.pledgePrice / self.quantity, 2)
        return percentage_from(number=result, percent=25)
