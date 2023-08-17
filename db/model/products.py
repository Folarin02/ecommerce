from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..db_setup import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), unique=True, nullable=False)
    category = Column(String(50))
    original_price = Column(Integer, default=True)
    new_price = Column(Integer, default=True)
    discount = Column(Integer)
    offer_expiration_date = Column(default=datetime.utcnow)
    


