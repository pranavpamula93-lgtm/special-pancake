from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import DECIMAL


class PromotionsBase(BaseModel):
    id: int
    promo_code: str
    expiration_date: datetime

class PromotionsCreate(PromotionsBase):
    pass

class PromotionsUpdate(BaseModel):
    id: Optional[int] = None
    promo_code: Optional[str] = None
    expiration_date: Optional[datetime] = None

class Promotions(PromotionsBase):
    id: int

    class ConfigDict:
        from_attributes = True
