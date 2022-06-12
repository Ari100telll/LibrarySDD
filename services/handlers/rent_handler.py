from abc import ABC, abstractmethod

from models.rent import Rent
from services.payment.payment_strategy import PaymentStrategy


class RentHandler(ABC):
    @abstractmethod
    def set_next(self, next_handler: "RentHandler") -> "RentHandler":
        pass

    @abstractmethod
    def handle(self, rent: Rent, payment_strategy: PaymentStrategy):
        pass
