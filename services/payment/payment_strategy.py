from abc import ABC, abstractmethod
from decimal import Decimal
from enum import Enum
from typing import Any


class PaymentStrategyEnum(Enum):
    CARD_PAYMENT = "CARD"
    BANK_ACCOUNT_PAYMENT = "BANK ACCOUNT"


class PaymentStrategy(ABC):
    @abstractmethod
    def make_payment(
        self, amount: Decimal, user: Any
    ):  # TODO: replace user field type to the User model
        pass
