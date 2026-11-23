from decimal import Decimal

from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Float
from sqlalchemy.orm import relationship
from datetime import datetime

from ..dependencies.database import Base

class MenuItems(Base):
    __tablename__ = "menu_items"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dishes = Column(String(300))
    ingredients = Column(String(300))
    price = Column(Float)
    calories = Column(Integer)
    food_category = Column(String(300))

    orders = relationship("Order", back_populates="menu_items")