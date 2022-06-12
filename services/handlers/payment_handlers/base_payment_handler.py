from abc import ABC

from services.commands.make_payment_command import MakePaymentCommand
from services.handlers.rent_handler import RentHandler


class BasePaymentHandler(RentHandler, ABC):
    def __init__(
        self,
        command: MakePaymentCommand = None,
        next_handler: "BasePaymentHandler" = None,
    ):
        self.command: MakePaymentCommand = command
        self.next_handler: BasePaymentHandler = next_handler
