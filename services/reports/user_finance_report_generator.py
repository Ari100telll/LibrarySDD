from typing import List

from models.rent import Rent
from schemas.library_item_schema import library_item_schema
from utils.helpers import percentage_from


class UserFinanceReportGenerator:
    def __init__(self, rents: List[Rent]):
        self.rents = rents

    def generate(self):
        rents_finance_info = [self.retrieve_finance_info(rent) for rent in self.rents]
        aggregated_finance_info = self.aggregate_finance_info(rents_finance_info)

        finance_report = {
            "rents": rents_finance_info,
            "aggregated": aggregated_finance_info,
        }

        return finance_report

    def retrieve_finance_info(self, rent):
        discount_percentage = rent.library_user.reader_category.discount_percentage
        discount_price = percentage_from(rent.rent_price, discount_percentage)
        finance_info = {
            "rent_start_date": rent.rent_start_date,
            "expected_rent_end_date": rent.expected_rent_end_date,
            "rent_end_date": rent.rent_end_date,
            "pledge_price": rent.library_item.pledge_price,
            "discount_percentage": discount_percentage,
            "discount_price": discount_price,
            "rent_price_after_discount": rent.rent_price,
            "rent_price_before_discount": rent.rent_price + discount_price,
            "damage_fine_percentage": rent.damage_level.fine_percentage,
            "fine_price": rent.fine_price,
            "total_price": rent.fine_price + rent.rent_price,
            "library_item": library_item_schema.dump(rent.library_item),
        }
        return finance_info

    def aggregate_finance_info(self, finance_info):
        total_paid_rent = sum(
            info["rent_price_after_discount"]
            for info in finance_info
            if info["rent_end_date"]
        )
        total_paid_pledge = sum(
            info["pledge_price"] for info in finance_info if not info["rent_end_date"]
        )
        total_paid_fine = sum(
            info["fine_price"] for info in finance_info if info["rent_end_date"]
        )
        total_unpaid_rent = sum(
            info["rent_price_after_discount"]
            for info in finance_info
            if not info["rent_end_date"]
        )
        total_unpaid_fine = sum(
            info["fine_price"] for info in finance_info if not info["rent_end_date"]
        )
        total_discount_price = sum(info["discount_price"] for info in finance_info)

        aggregated_finance_info = {
            "total_paid_rent": total_paid_rent,
            "total_paid_pledge": total_paid_pledge,
            "total_paid_fine": total_paid_fine,
            "total_paid": total_paid_rent + total_paid_pledge + total_paid_fine,
            "total_unpaid_rent": total_unpaid_rent,
            "total_unpaid_fine": total_unpaid_fine,
            "total_unpaid": total_unpaid_rent + total_unpaid_fine,
            "total_discount_price": total_discount_price,
        }

        return aggregated_finance_info
