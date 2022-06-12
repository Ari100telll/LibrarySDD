from models.rent import Rent
from services.commands.rent_command import RentCommand
from services.handlers.payment_handlers.base_payment_handler import BasePaymentHandler
from services.handlers.payment_handlers.pay_fine_handler import PayFineHandler
from services.handlers.payment_handlers.pay_rent_handler import PayRentHandler
from services.payment.payment_strategy import PaymentStrategy


class RentReturnPaymentCommand(RentCommand):
    def __init__(self):
        self.rent_payment_handler: BasePaymentHandler = PayRentHandler()
        self.rent_payment_handler.set_next(PayFineHandler())

    def execute(self, rent: Rent, payment_strategy: PaymentStrategy):
        self.rent_payment_handler.handle(rent, payment_strategy)
