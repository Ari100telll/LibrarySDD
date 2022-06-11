from sqlalchemy import Column, Integer, Numeric, String

import utils.db


class DamageLevel(utils.db.Base):
    __tablename__ = "damage_level"
    id = Column(Integer, primary_key=True)
    level = Column(String(30))
    fine_percentage = Column(Numeric)

    def __repr__(self):
        return str(self.__dict__)
