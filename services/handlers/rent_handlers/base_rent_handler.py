from abc import ABC

from models.rent import Rent
from services.commands.rent_command import RentCommand
from services.handlers.rent_handler import RentHandler
from services.payment.payment_strategy import PaymentStrategy


class BaseRentHandler(RentHandler, ABC):
    def __init__(self, command: RentCommand, next_handler: "BaseRentHandler" = None):
        self.command: RentCommand = command
        self.next_handler: BaseRentHandler = next_handler

    def set_next(self, next_handler: RentHandler):
        self.next_handler = next_handler
        return next_handler

    def handle(self, rent: Rent, payment_strategy: PaymentStrategy):
        self.command.execute(rent, payment_strategy)
        if self.next_handler:
            self.next_handler.handle(rent, payment_strategy)
