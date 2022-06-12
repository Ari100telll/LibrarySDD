from abc import ABC

from services.commands.rent_command import RentCommand
from services.handlers.rent_handler import RentHandler


class BaseRentHandler(RentHandler, ABC):
    def __init__(
        self, next_handler: "BaseRentHandler" = None, command: RentCommand = None
    ):
        self.next_handler: BaseRentHandler = next_handler
        self.command: RentCommand = command
