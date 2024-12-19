from typing import Optional
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base

#таблица айфонов в базе данных
class  Iphones(Base):
    __tablename__ = 'iphones'
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable= False)
    battery = Column(Integer, nullable = False)
    owner = Column(String, nullable = False)

