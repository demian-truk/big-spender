from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Income(Base):
    __tablename__ = "income"
    id = Column(Integer, primary_key=True)
    amount = Column(Float)


class Expense(Base):
    __tablename__ = "expense"
    id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    created_at = Column(DateTime)
    category_id = Column(ForeignKey("category.id"))
    category = relationship("Category", back_populates="expenses")


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    expenses = relationship(Expense, back_populates="category")
