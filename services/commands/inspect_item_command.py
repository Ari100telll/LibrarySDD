from models.rent import Rent
from services.commands.rent_command import RentCommand
from services.observer.library_publisher import LibraryPublisher
from services.payment.payment_strategy import PaymentStrategy


class InspectItemCommand(RentCommand):
    def execute(self, rent: Rent, payment_strategy: PaymentStrategy):
        def callback(damage_level):
            rent.damage_level = damage_level

        library_publisher = LibraryPublisher()
        library_publisher.add_item_to_inspect(rent.library_item, callback)
