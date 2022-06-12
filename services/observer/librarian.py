import random

from models.damage_level import DamageLevel
from services.observer.subscriber import Subscriber


class Librarian(Subscriber):
    def update(self, context, callback):
        self.inspect_library_item(context, callback)

    def inspect_library_item(self, context, callback):
        context.items_to_inspect.pop()

        damage_levels = DamageLevel.query.all()
        random_damage_level = random.choice(damage_levels)

        callback(random_damage_level)
