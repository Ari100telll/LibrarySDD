from abc import ABC, abstractmethod
from decimal import Decimal
from enum import Enum

from models.user import User


class PaymentStrategyEnum(Enum):
    CARD_PAYMENT = "CARD"
    BANK_ACCOUNT_PAYMENT = "BANK ACCOUNT"


class PaymentStrategy(ABC):
    @abstractmethod
    def make_payment(self, amount: Decimal, user: User):
        pass
