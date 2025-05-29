from sqlalchemy import Column, Integer, String

from db import Base


class Noivo(Base):
    __tablename__ = 'noivo'

    noivo_id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    senha = Column(String, nullable=False)
