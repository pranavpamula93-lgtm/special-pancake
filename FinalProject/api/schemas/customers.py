from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

from .reviews import Reviews

class CustomerBase(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    id: int
    customer_name: str
    email: str
    phone_number: int
    address: str
    review: int

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    customer_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[int] = None
    address: Optional[str] = None

class Customer(CustomerBase):
    id: int
    review: Optional[Reviews] = None

    class ConfigDict:
        from_attributes = True

