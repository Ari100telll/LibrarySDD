from typing import List

from models.library_item import LibraryItem
from models.rent import Rent
from services.factory.library_item_factory import LibraryItemFactory
from services.reports.user_finance_report_generator import UserFinanceReportGenerator


class ReportManager:
    def __init__(self, library_item_factory: LibraryItemFactory):
        self.library_item_factory = library_item_factory

    def get_library_items(self) -> List[LibraryItem]:
        return self.library_item_factory.get_library_items()

    @staticmethod
    def get_rents(user_id: int) -> List[Rent]:
        return Rent.query.filter_by(library_user_id=user_id)

    @classmethod
    def get_user_financial_report(cls, user_id: int):
        user_rents = cls.get_rents(user_id)
        return UserFinanceReportGenerator(user_rents).generate()
