from services.commands.rent_return_payment_command import RentReturnPaymentCommand
from services.handlers.rent_handlers.base_rent_handler import BaseRentHandler


class RentReturnPaymentHandler(BaseRentHandler):
    def __init__(self):
        super().__init__(command=RentReturnPaymentCommand())
