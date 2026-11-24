from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Customers(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    email = Column(String(200))
    phone_number = Column(Integer)
    address = Column(String(300))
    review_id = Column(Integer, ForeignKey('reviews.id'))

    reviews = relationship("Reviews", back_populates="customers")
    orders = relationship("Order", back_populates="customers")