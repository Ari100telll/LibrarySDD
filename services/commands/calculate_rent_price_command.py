from datetime import datetime
from decimal import Decimal

from models.rent import Rent
from services.commands.rent_command import RentCommand
from services.payment.payment_strategy import PaymentStrategy


class CalculateRentPriceCommand(RentCommand):
    def execute(self, rent: Rent, payment_strategy: PaymentStrategy):
        rent_start_datetime = datetime.fromordinal(rent.rent_start_date.toordinal())
        expected_end_datetime = datetime.fromordinal(
            rent.expected_rent_end_date.toordinal()
        )
        rent_days_number = (rent_start_datetime - expected_end_datetime).days
        rent.rent_price = Decimal(
            rent.library_item.calculate_rent_price_per_day() * rent_days_number
        )
