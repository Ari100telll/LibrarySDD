from decimal import Decimal

from config.settings.strings import PROCESSING_PAYMENT_MESSAGE
from models.user import User
from services.payment.payment_strategy import PaymentStrategy


class PaymentManager(object):
    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy: PaymentStrategy = payment_strategy

    def set_strategy(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def process_payment(self, amount: Decimal, user: User):
        print(PROCESSING_PAYMENT_MESSAGE.format(user_phone_number=user.phone_number))
        self.payment_strategy.make_payment(amount, user)
