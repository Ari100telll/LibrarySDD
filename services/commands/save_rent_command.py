from models.rent import Rent
from resources import db
from services.commands.rent_command import RentCommand
from services.payment.payment_strategy import PaymentStrategy


class SaveRentCommand(RentCommand):
    def execute(self, rent: Rent, payment_strategy: PaymentStrategy):
        db.session.commit()
