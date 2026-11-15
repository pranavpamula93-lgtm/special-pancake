from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

from schemas.orders import Order
from schemas.promotions import Promotions


class PaymentsBase(BaseModel):
    id: int
    card_information: str
    transaction_status: str
    payment_type: str
    promo_id: int
    order_id: int

class PaymentsCreate(PaymentsBase):
    pass

class PaymentsUpdate(BaseModel):
    card_information: Optional[str] = None
    transaction_status: Optional[str] = None
    payment_type: Optional[str] = None
    promo_id: Optional[int] = None
    order_id: Optional[str] = None

class Payments(PaymentsBase):
    id: int
    order: Optional[Order] = None
    promotion: Optional[Promotions] = None

    class ConfigDict:
        from_attributes = True