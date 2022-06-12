from models.rent import Rent
from services.commands.rent_command import RentCommand
from services.handlers.payment_handlers.base_payment_handler import BasePaymentHandler
from services.handlers.payment_handlers.pay_pledge_handler import PayPledgeHandler
from services.payment.payment_strategy import PaymentStrategy


class RentRequestPaymentCommand(RentCommand):
    def __init__(self):
        self.pledge_payment_handler: BasePaymentHandler = PayPledgeHandler()

    def execute(self, rent: Rent, payment_strategy: PaymentStrategy):
        self.pledge_payment_handler.handle(rent, payment_strategy)
