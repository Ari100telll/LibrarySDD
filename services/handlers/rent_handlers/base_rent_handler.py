from abc import ABC

from services.commands.rent_command import RentCommand
from services.handlers.rent_handler import RentHandler


class BaseRentHandler(RentHandler, ABC):
    def __init__(self, command: RentCommand, next_handler: "BaseRentHandler" = None):
        self.command: RentCommand = command
        self.next_handler: BaseRentHandler = next_handler
