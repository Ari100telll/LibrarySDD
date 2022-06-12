from services.commands.inspect_item_command import InspectItemCommand
from services.handlers.rent_handlers.base_rent_handler import BaseRentHandler


class InspectItemHandler(BaseRentHandler):
    def __init__(self):
        super().__init__(command=InspectItemCommand())
