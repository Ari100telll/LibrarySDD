from decimal import Decimal

from models.rent import Rent
from services.commands.rent_command import RentCommand
from services.payment.payment_manager import PaymentManager
from services.payment.payment_strategy import PaymentStrategy


class MakePaymentCommand(RentCommand):
    def __init__(self, amount: Decimal):
        self.amount: Decimal = amount

    def execute(self, rent: Rent, payment_strategy: PaymentStrategy):
        payment_manager: PaymentManager = PaymentManager(payment_strategy)
        payment_manager.process_payment(self.amount, rent.library_user)
