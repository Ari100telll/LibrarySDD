from abc import ABC
from decimal import Decimal

from services.commands.make_payment_command import MakePaymentCommand
from services.handlers.rent_handler import RentHandler


class BasePaymentHandler(RentHandler, ABC):
    def __init__(self):
        self.next_handler: BasePaymentHandler = BasePaymentHandler()
        self.command: MakePaymentCommand = MakePaymentCommand(Decimal(0))
