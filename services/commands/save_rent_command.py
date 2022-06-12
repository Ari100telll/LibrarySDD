from models.rent import Rent
from resources import db
from services.commands.rent_command import RentCommand
from services.payment.payment_strategy import PaymentStrategy


class SaveRentCommand(RentCommand):
    def execute(self, rent: Rent, payment_strategy: PaymentStrategy):
        exists = db.session.query(Rent).filter_by(id=rent.id).exists()
        if not exists:
            db.session.add(rent)
        db.session.commit()
