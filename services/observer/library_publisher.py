from typing import List

from models.library_item import LibraryItem
from services.observer.subscriber import Subscriber
from services.singleton.singleton import singleton


@singleton
class LibraryPublisher:
    def __init__(self):
        self.subscribers: List[Subscriber] = []
        self.items_to_inspect: List[LibraryItem] = []

    def subscribe(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)

    def __notify_subscribers(self, callback):
        for subscriber in self.subscribers:
            subscriber.update(self, callback)

    def add_item_to_inspect(self, item: LibraryItem, callback):
        self.items_to_inspect.append(item)
        self.__notify_subscribers(callback)
