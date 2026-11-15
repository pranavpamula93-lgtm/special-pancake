from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    tracking_number = Column(Integer)
    total_price = Column(Float)
    order_status = Column(String(100))
    menu_id = Column(Integer, ForeignKey('menu_items.id'))
    resource_id = Column(Integer, ForeignKey('resources.id'))

    menu_items = relationship("MenuItems", back_populates="orders")
    resources = relationship("Resources", back_populates="orders")
    payments = relationship("Payments", back_populates="orders")
    customer = relationship("Customers", back_populates="orders")