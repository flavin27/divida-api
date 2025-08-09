from sqlalchemy import Column, Integer, String
from Database.db import Base

class DimNaturezaDivida(Base):
    __tablename__ = "dim_natureza_dividas"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    descricao = Column(String)
