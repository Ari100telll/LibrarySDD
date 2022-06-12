import random

from models.damage_level import DamageLevel, DamageLevelValues
from services.observer.subscriber import Subscriber


class Librarian(Subscriber):
    def update(self, context, callback):
        self.inspect_library_item(context, callback)

    def inspect_library_item(self, context, callback):
        context.items_to_inspect.pop()

        level = random.choice(list(DamageLevelValues))
        random_damage_level = DamageLevel.query.filter_by(level=level.name).first()

        callback(random_damage_level)
