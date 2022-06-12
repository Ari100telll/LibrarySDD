from models.rent import Rent
from services.commands.rent_command import RentCommand
from services.payment.payment_strategy import PaymentStrategy


class UpdateBookCatalogueCommand(RentCommand):
    def execute(self, rent: Rent, payment_strategy: PaymentStrategy):
        if not rent.rent_end_date:
            items_difference = -1
        else:
            items_difference = 1
        rent.library_item.quantity += items_difference

        return rent, payment_strategy
