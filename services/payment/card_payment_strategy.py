from decimal import Decimal

from config.settings.strings import BASE_PAYMENT_MESSAGE, PAYMENT_TAG_STRING_MAX_LEN
from models.user import User
from services.payment.payment_strategy import PaymentStrategy, PaymentStrategyEnum


class CardPaymentStrategy(PaymentStrategy):
    def make_payment(self, amount: Decimal, user: User):
        print(
            BASE_PAYMENT_MESSAGE.format(
                method=PaymentStrategyEnum.CARD_PAYMENT.value.ljust(
                    PAYMENT_TAG_STRING_MAX_LEN
                ),
                amount=amount,
                user_full_name=str(user.name + " " + user.surname),
                user_phone_number=user.phone_number,
            )
        )
