from models.rent import Rent
from services.commands.rent_request_payment_command import RentRequestPaymentCommand
from services.handlers.rent_handlers.base_rent_handler import BaseRentHandler
from services.payment.payment_strategy import PaymentStrategy


class RentRequestPaymentHandler(BaseRentHandler):
    def __init__(self):
        super().__init__(command=RentRequestPaymentCommand())

    def set_next(self, next_handler: BaseRentHandler) -> BaseRentHandler:
        self.next_handler = next_handler
        return self.next_handler

    def handle(self, rent: Rent, payment_strategy: PaymentStrategy):
        self.command.execute(rent, payment_strategy)
        if self.next_handler:
            self.next_handler.handle(rent, payment_strategy)