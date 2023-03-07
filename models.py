from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Income(Base):
    __tablename__ = "income"
    id = Column(Integer, primary_key=True)
    amount = Column(Float)


class Expense(Base):
    __tablename__ = "expense"
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    created_at = Column(DateTime, default=datetime.now())
    category = Column(ForeignKey("category.name"))
    category_id = Column(ForeignKey("category.id"))


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    name = Column(String)
