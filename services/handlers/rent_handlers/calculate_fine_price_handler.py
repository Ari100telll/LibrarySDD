from models.rent import Rent
from services.commands.calculate_fine_price_command import CalculateFinePriceCommand
from services.handlers.rent_handler import RentHandler
from services.handlers.rent_handlers.base_rent_handler import BaseRentHandler
from services.payment.payment_strategy import PaymentStrategy


class CalculateFinePriceHandler(BaseRentHandler):
    def __init__(self):
        super().__init__(command=CalculateFinePriceCommand())

    def set_next(self, next_handler: RentHandler):
        self.next_handler = next_handler

    def handle(self, rent: Rent, payment_strategy: PaymentStrategy):
        self.command.execute(rent, payment_strategy)
        if self.next_handler:
            self.next_handler.handle(rent, payment_strategy)
