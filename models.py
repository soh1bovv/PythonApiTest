from typing import Optional
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy import declarative_base

#базовый класс для обьявления моделей данных
Base = declarative_base()

#таблица айфонов в базе данных
class  Iphones(Base):
    __tablename__ = 'iphones'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    battery = Column(Integer)
    owner = Column(String)
