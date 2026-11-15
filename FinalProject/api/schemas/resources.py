from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ResourcesBase(BaseModel):
    id: int
    resource_amount: int

class ResourcesCreate(ResourcesBase):
    pass

class ResourcesUpdate(BaseModel):
    id: Optional[int] = None
    resource_amount: Optional[int] = None

class Resources(ResourcesBase):
    id: int

    class ConfigDict:
        from_attributes = True
