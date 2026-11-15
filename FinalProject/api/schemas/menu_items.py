from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict
from sqlalchemy import DECIMAL, Float


class MenuItemsBase(BaseModel):
    id: int
    dishes: str
    ingredients: str
    price: float
    calories: int
    food_category: str

class MenuItemsCreate(MenuItemsBase):
    pass

class MenuItemsUpdate(BaseModel):
    dishes: Optional[str] = None
    ingredients: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    food_category: Optional[str] = None

class MenuItems(MenuItemsBase):
    id: int

    class ConfigDict:
        from_attributes = True


