from resources import db
from utils.helpers import percentage_from

DAILY_RENT_PRICE_PERCENT = 25


class LibraryItem(db.Model):
    __tablename__ = "library_item"
    id = db.Column(db.Integer, primary_key=True)
    pledge_price = db.Column(db.Numeric)
    quantity = db.Column(db.Integer)

    def __repr__(self):
        return str(self.__dict__)

    @staticmethod
    def from_dict(body: dict):
        pledge_price = body["pledge_price"]
        quantity = body["quantity"]
        return LibraryItem(pledge_price=pledge_price, quantity=quantity)

    def calculate_rent_price_per_day(self) -> float:
        result = round(self.pledge_price / self.quantity, 2)
        return percentage_from(number=result, percent=DAILY_RENT_PRICE_PERCENT)
