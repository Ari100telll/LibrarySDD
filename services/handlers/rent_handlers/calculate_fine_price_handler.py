from services.commands.calculate_fine_price_command import CalculateFinePriceCommand
from services.handlers.rent_handlers.base_rent_handler import BaseRentHandler


class CalculateFinePriceHandler(BaseRentHandler):
    def __init__(self):
        super().__init__(command=CalculateFinePriceCommand())
