from models.rent import Rent
from services.commands.make_payment_command import MakePaymentCommand
from services.handlers.payment_handlers.base_payment_handler import BasePaymentHandler
from services.payment.payment_strategy import PaymentStrategy


class PayPledgeHandler(BasePaymentHandler):
    def __init__(self):
        super().__init__()

    def set_next(self, next_handler: BasePaymentHandler):
        self.next_handler = next_handler

    def handle(self, rent: Rent, payment_strategy: PaymentStrategy):
        self.command = MakePaymentCommand(rent.library_item.pledge_price)
        self.command.execute(rent, payment_strategy)
