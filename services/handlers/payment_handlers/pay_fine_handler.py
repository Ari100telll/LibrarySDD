from decimal import Decimal

from models.rent import Rent
from services.commands.make_payment_command import MakePaymentCommand
from services.handlers.payment_handlers.base_payment_handler import BasePaymentHandler
from services.payment.payment_strategy import PaymentStrategy


class PayFineHandler(BasePaymentHandler):
    def handle(self, rent: Rent, payment_strategy: PaymentStrategy):
        self.command = MakePaymentCommand(Decimal(rent.fine_price))
        self.command.execute(rent, payment_strategy)
        if self.next_handler:
            self.next_handler.handle(rent, payment_strategy)
