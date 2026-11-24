from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Payments(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    card_information = Column(String(300))
    transaction_status = Column(String(300))
    payment_type = Column(String(100))
    promo_id = Column(Integer, ForeignKey('promotions.id'))
    order_id = Column(Integer, ForeignKey('orders.id'))

    orders = relationship("Order", back_populates="payments")
    promotions = relationship("Promotions", back_populates="payments")