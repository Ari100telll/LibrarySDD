from models.rent import Rent
from services.commands.rent_command import RentCommand
from services.payment.payment_strategy import PaymentStrategy
from utils.helpers import percentage_from


class CalculateFinePriceCommand(RentCommand):
    def execute(self, rent: Rent, payment_strategy: PaymentStrategy):
        fine_price = percentage_from(
            number=rent.library_item.pledge_price,
            percent=rent.damage_level.fine_percentage,
        )
        rent.fine_price = fine_price
