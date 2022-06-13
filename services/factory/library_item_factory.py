from abc import ABC, abstractmethod
from typing import List

from models.library_item import LibraryItem


class LibraryItemFactory(ABC):
    @abstractmethod
    def create_library_item(self, body: dict) -> LibraryItem:
        pass

    @abstractmethod
    def get_library_items(self) -> List[LibraryItem]:
        pass

    @abstractmethod
    def get_library_item_by(self, item_id: int) -> LibraryItem:
        pass

    @abstractmethod
    def delete_library_item(self, item_id: int) -> None:
        pass

    @abstractmethod
    def update_library_item(self, item_id: int, body: dict) -> LibraryItem:
        pass
