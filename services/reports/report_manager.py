from typing import List

from models.rent import Rent
from services.reports.report_generator import ReportGenerator


class ReportManager:
    @staticmethod
    def get_rents(user_id: int) -> List[Rent]:
        return Rent.query.filter_by(library_user_id=user_id)

    @classmethod
    def get_user_financial_report(cls, user_id: int):
        user_rents = cls.get_rents(user_id)
        return ReportGenerator(user_rents).generate_user_report()

    @staticmethod
    def get_library_financial_report():
        rents = Rent.query.all()
        return ReportGenerator(rents).generate_library_report()
