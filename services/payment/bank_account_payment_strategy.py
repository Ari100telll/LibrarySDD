from decimal import Decimal
from typing import Any

from config.settings.strings import BASE_PAYMENT_MESSAGE, PAYMENT_METHOD_STRING_MAX_LEN
from services.payment.payment_strategy import PaymentStrategy, PaymentStrategyEnum


class BankAccountPaymentStrategy(PaymentStrategy):
    def make_payment(self, amount: Decimal, user: Any):
        # TODO: mocked user data
        user = dict(name="Killroy", surname="Smith", phone_number="+38 (044) 255 7333")
        print(
            BASE_PAYMENT_MESSAGE.format(
                method=PaymentStrategyEnum.BANK_ACCOUNT_PAYMENT.value.ljust(
                    PAYMENT_METHOD_STRING_MAX_LEN
                ),
                amount=amount,
                user_full_name=str(user.get("name") + user.get("surname")),
                user_phone_number=user.get("phone_number"),
            )
        )
