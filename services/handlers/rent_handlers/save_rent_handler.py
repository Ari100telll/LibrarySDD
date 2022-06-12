from services.commands.save_rent_command import SaveRentCommand
from services.handlers.rent_handlers.base_rent_handler import BaseRentHandler


class SaveRentHandler(BaseRentHandler):
    def __init__(self):
        super().__init__(command=SaveRentCommand())
