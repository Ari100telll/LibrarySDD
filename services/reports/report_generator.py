from typing import List

from models.rent import Rent
from schemas.library_item_schema import library_item_schema
from schemas.user_schema import user_schema
from utils.helpers import percentage_from

user_aggregated_keys = [
    "total_paid_rent",
    "total_paid_pledge",
    "total_paid_fine",
    "total_paid",
    "total_unpaid_rent",
    "total_unpaid_fine",
    "total_unpaid",
    "total_discount_price",
]

library_aggregated_keys = [
    "total_received_rent_price",
    "total_received_pledge_price",
    "total_received_fine_price",
    "total_received",
    "total_pending_rent_price",
    "total_pending_fine_price",
    "total_pending",
    "total_discount_price",
]


class ReportGenerator:
    def __init__(self, rents: List[Rent]):
        self.rents = rents

    def generate_user_report(self):
        return self.generate(user_aggregated_keys, should_include_user=False)

    def generate_library_report(self):
        return self.generate(library_aggregated_keys, should_include_user=True)

    def generate(
        self, aggregated_keys: List[str], should_include_user: bool = False
    ) -> dict:
        finance_info = [
            self.retrieve_finance_info(rent, should_include_user) for rent in self.rents
        ]
        aggregated_finance_info = self.aggregate_finance_info(
            finance_info, aggregated_keys
        )

        finance_report = {
            "rents": finance_info,
            "aggregated": aggregated_finance_info,
        }

        return finance_report

    def retrieve_finance_info(self, rent, should_include_user=False) -> dict:
        discount_percentage = rent.library_user.reader_category.discount_percentage
        discount_price = percentage_from(rent.rent_price, discount_percentage)

        finance_info = {
            "id": rent.id,
            "rent_start_date": rent.rent_start_date,
            "expected_rent_end_date": rent.expected_rent_end_date,
            "rent_end_date": rent.rent_end_date,
            "pledge_price": rent.library_item.pledge_price,
            "discount_percentage": discount_percentage,
            "discount_price": discount_price,
            "rent_price_after_discount": rent.rent_price,
            "rent_price_before_discount": rent.rent_price + discount_price,
            "damage_fine_percentage": rent.damage_level.fine_percentage
            if rent.damage_level
            else 0,
            "fine_price": rent.fine_price if rent.fine_price else 0,
            "total_price": (rent.fine_price if rent.fine_price else 0)
            + rent.rent_price,
            "library_item": library_item_schema.dump(rent.library_item),
        }

        if should_include_user:
            finance_info["user"] = user_schema.dump(rent.library_user)

        return finance_info

    def aggregate_finance_info(self, rents: List[dict], keys: List[str]) -> dict:
        paid_rent = sum(
            rent["rent_price_after_discount"] for rent in rents if rent["rent_end_date"]
        )
        paid_pledge = sum(
            rent["pledge_price"] for rent in rents if not rent["rent_end_date"]
        )
        paid_fine = sum(rent["fine_price"] for rent in rents if rent["rent_end_date"])
        paid_total = paid_rent + paid_pledge + paid_fine
        unpaid_rent = sum(
            rent["rent_price_after_discount"]
            for rent in rents
            if not rent["rent_end_date"]
        )
        unpaid_fine = sum(
            rent["fine_price"] for rent in rents if not rent["rent_end_date"]
        )
        unpaid_total = unpaid_rent + unpaid_fine
        discount_price = sum(rent["discount_price"] for rent in rents)

        values = [
            paid_rent,
            paid_pledge,
            paid_fine,
            paid_total,
            unpaid_rent,
            unpaid_fine,
            unpaid_total,
            discount_price,
        ]

        return dict(zip(keys, values))
