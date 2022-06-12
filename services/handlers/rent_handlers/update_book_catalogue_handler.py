from services.commands.update_book_catalogue_command import UpdateBookCatalogueCommand
from services.handlers.rent_handlers.base_rent_handler import BaseRentHandler


class UpdateBookCatalogueHandler(BaseRentHandler):
    def __init__(self):
        super().__init__(command=UpdateBookCatalogueCommand())
