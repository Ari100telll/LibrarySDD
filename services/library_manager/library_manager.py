from datetime import datetime

from models.library_item import LibraryItem
from models.rent import Rent
from models.user import User
from services.handlers.rent_handlers.apply_discount_handler import ApplyDiscountHandler
from services.handlers.rent_handlers.calculate_fine_price_handler import (
    CalculateFinePriceHandler,
)
from services.handlers.rent_handlers.calculate_rent_price_handler import (
    CalculateRentPriceHandler,
)
from services.handlers.rent_handlers.inspect_item_handlers import InspectItemHandler
from services.handlers.rent_handlers.rent_request_payment_handler import (
    RentRequestPaymentHandler,
)
from services.handlers.rent_handlers.rent_return_payment_handler import (
    RentReturnPaymentHandler,
)
from services.handlers.rent_handlers.save_rent_handler import SaveRentHandler
from services.handlers.rent_handlers.update_book_catalogue_handler import (
    UpdateBookCatalogueHandler,
)
from services.payment.bank_account_payment_strategy import BankAccountPaymentStrategy
from services.payment.card_payment_strategy import CardPaymentStrategy
from services.payment.payment_strategy import PaymentStrategy
from services.singleton.singleton import singleton


@singleton
class LibraryManager:
    @classmethod
    def rent_library_item(
        cls,
        library_item: LibraryItem,
        user: User,
        expected_rent_end_date: datetime,
        payment_type: str,
    ):
        rent = cls.__create_rent(
            library_item=library_item,
            user=user,
            expected_rent_end_date=expected_rent_end_date,
        )

        payment_strategy = cls.__get_payment_strategy_from_type(payment_type)

        handler = cls.__get_rent_request_handlers()
        handler.handle(rent, payment_strategy)

        return rent

    @classmethod
    def return_library_item(
        cls,
        rent: Rent,
        payment_type: str,
    ):
        rent.rent_end_date = datetime.utcnow().date()
        payment_strategy = cls.__get_payment_strategy_from_type(payment_type)

        handler = cls.__get_rent_return_handlers()
        handler.handle(rent, payment_strategy)

        return rent

    @staticmethod
    def __create_rent(
        library_item: LibraryItem,
        user: User,
        expected_rent_end_date: datetime,
    ) -> Rent:
        rent = Rent(
            library_item=library_item,
            library_user=user,
            rent_start_date=datetime.utcnow(),
            expected_rent_end_date=expected_rent_end_date,
        )
        return rent

    @staticmethod
    def __get_rent_request_handlers():
        handler = CalculateRentPriceHandler()
        handler.set_next(ApplyDiscountHandler()).set_next(
            RentRequestPaymentHandler()
        ).set_next(UpdateBookCatalogueHandler()).set_next(SaveRentHandler())
        return handler

    @staticmethod
    def __get_rent_return_handlers():
        handler = InspectItemHandler()
        handler.set_next(CalculateFinePriceHandler()).set_next(
            RentReturnPaymentHandler()
        ).set_next(UpdateBookCatalogueHandler()).set_next(SaveRentHandler())
        return handler

    @staticmethod
    def __get_payment_strategy_from_type(payment_type: str) -> PaymentStrategy:
        if payment_type == "card":
            payment_strategy = CardPaymentStrategy()
        else:
            payment_strategy = BankAccountPaymentStrategy()
        return payment_strategy
