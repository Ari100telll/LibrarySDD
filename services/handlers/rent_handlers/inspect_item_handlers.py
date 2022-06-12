from models.rent import Rent
from services.commands.inspect_item_command import InspectItemCommand
from services.handlers.rent_handler import RentHandler
from services.handlers.rent_handlers.base_rent_handler import BaseRentHandler
from services.payment.payment_strategy import PaymentStrategy


class InspectItemHandler(BaseRentHandler):
    def set_next(self, next_handler: RentHandler):
        self.next_handler = next_handler

    def handle(self, rent: Rent, payment_strategy: PaymentStrategy):
        self.command = InspectItemCommand()
        self.command.execute(rent, payment_strategy)
        if self.next_handler:
            self.next_handler.handle(rent, payment_strategy)
