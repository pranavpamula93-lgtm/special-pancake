from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ReviewsBase(BaseModel):
    id: int
    rating: float
    review: str

class ReviewsCreate(ReviewsBase):
    pass

class ReviewsUpdate(BaseModel):
    id: Optional[int] = None
    resource_amount: Optional[int] = None

class Reviews(ReviewsBase):
    id: int

    class ConfigDict:
        from_attributes = True
