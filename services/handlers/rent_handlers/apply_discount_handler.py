from services.commands.apply_discount_command import ApplyDiscountCommand
from services.handlers.rent_handlers.base_rent_handler import BaseRentHandler


class ApplyDiscountHandler(BaseRentHandler):
    def __init__(self):
        super().__init__(command=ApplyDiscountCommand())
