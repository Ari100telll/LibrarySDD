from services.commands.calculate_rent_price_command import CalculateRentPriceCommand
from services.handlers.rent_handlers.base_rent_handler import BaseRentHandler


class CalculateRentPriceHandler(BaseRentHandler):
    def __init__(self):
        super().__init__(command=CalculateRentPriceCommand())
