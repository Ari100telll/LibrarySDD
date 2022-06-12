from abc import ABC

from services.commands.rent_command import RentCommand
from services.handlers.rent_handler import RentHandler


class BaseRentHandler(RentHandler, ABC):
    def __init__(self):
        self.next_handler: BaseRentHandler = BaseRentHandler()
        self.command: RentCommand = RentCommand()
