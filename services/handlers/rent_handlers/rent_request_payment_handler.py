from services.commands.rent_request_payment_command import RentRequestPaymentCommand
from services.handlers.rent_handlers.base_rent_handler import BaseRentHandler


class RentRequestPaymentHandler(BaseRentHandler):
    def __init__(self):
        super().__init__(command=RentRequestPaymentCommand())
