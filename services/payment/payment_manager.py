from decimal import Decimal
from typing import Any

from config.settings.strings import PROCESSING_PAYMENT_MESSAGE
from services.payment.payment_strategy import PaymentStrategy


class PaymentManager(object):
    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy: PaymentStrategy = payment_strategy

    def set_strategy(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    # TODO: replace user field type to the User model
    def process_payment(self, amount: Decimal, user: Any):
        # TODO: mocked user data
        user = dict(name="Killroy", surname="Smith", phone_number="+38 (044) 255 7333")
        print(
            PROCESSING_PAYMENT_MESSAGE.format(
                user_phone_number=user.get("phone_number")
            )
        )
        self.payment_strategy.make_payment(amount, user)
