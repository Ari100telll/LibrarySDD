from models.rent import Rent
from services.commands.rent_command import RentCommand
from services.payment.payment_strategy import PaymentStrategy


class ApplyDiscountCommand(RentCommand):
    def execute(self, rent: Rent, payment_strategy: PaymentStrategy):
        rent.rent_price = (
            rent.rent_price
            * rent.library_user.reader_category.discount_percentage
            / 100
        )
