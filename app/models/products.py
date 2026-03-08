from sqlalchemy import Column, Integer, String, Float, DateTime, uui
from sqlalchemy.sql import func
from app.db.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(uuid, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    order_items = relationship("OrderItem", back_populates="product") 
