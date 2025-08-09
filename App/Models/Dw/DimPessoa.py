from sqlalchemy import Column, Integer, String
from App.Enums.DocumentEnum import DocumentEnum
from Database.dw import Base
from sqlalchemy.types import Enum as SqlEnum 

class DimPessoa(Base):

    __tablename__ = 'dim_pessoas'

    id = Column(Integer, primary_key=True, autoincrement=False)
    nome = Column(String, nullable=False)
    documento = Column(String, nullable=True)
    tipo_documento = Column(SqlEnum(DocumentEnum), nullable=False)

