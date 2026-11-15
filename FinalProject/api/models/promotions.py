from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Promotions(Base):
    __tablename__ = "promotions"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promo_code = Column(String(100))
    expiration_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))

    payments = relationship("Payments", back_populates="promotions")