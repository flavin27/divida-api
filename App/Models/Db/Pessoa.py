from sqlalchemy import Column, Integer, String
from App.Enums.DocumentEnum import DocumentEnum
from Database.db import Base
from sqlalchemy.types import Enum as SqlEnum 

class Pessoa(Base):

    __tablename__ = 'pessoas'

    id = Column(Integer, primary_key=True, autoincrement=False)
    nome = Column(String, nullable=False)
    documento = Column(String, nullable=True)
    tipo_documento = Column(SqlEnum(DocumentEnum), nullable=False)

