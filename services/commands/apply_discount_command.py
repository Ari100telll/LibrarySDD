from models.rent import Rent
from services.commands.rent_command import RentCommand
from services.payment.payment_strategy import PaymentStrategy
from utils.helpers import percentage_from


class ApplyDiscountCommand(RentCommand):
    def execute(self, rent: Rent, payment_strategy: PaymentStrategy):
        rent.rent_price = percentage_from(
            number=rent.rent_price,
            percent=rent.library_user.reader_category.discount_percentage,
        )
