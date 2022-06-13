from abc import ABC, abstractmethod

from models.rent import Rent
from services.payment.payment_strategy import PaymentStrategy


class RentCommand(ABC):
    @abstractmethod
    def execute(self, rent: Rent, payment_strategy: PaymentStrategy):
        pass
