from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict
from sqlalchemy import DECIMAL, Float

from .customers import Customer
from .menu_items import MenuItems

class OrderBase(BaseModel):
    id: int
    customer_id: int
    order_date: datetime
    tracking_number: int
    total_price: float
    order_status: str
    menu_id: int
    resource_id: int

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    customer_id: Optional[str] = None
    order_status: Optional[str] = None

class Order(OrderBase):
    id: int
    customer: Optional[Customer] = None
    menu_item: Optional[MenuItems] = None


    class ConfigDict:
        from_attributes = True


