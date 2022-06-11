from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from config.settings.base import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()


def init_db():
    from models.book import Book
    from models.damage_level import DamageLevel
    from models.library_item import LibraryItem
    from models.reader_category import ReaderCategory
    from models.rent import Rent
    from models.user import User

    Base.metadata.create_all(engine)
