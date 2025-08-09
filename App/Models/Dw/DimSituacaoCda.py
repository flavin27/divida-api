from sqlalchemy import Column, Integer, String
from Database.dw import Base

class DimSituacaoCda(Base):
    __tablename__ = "dim_situacao_cdas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cod_situacao_cda = Column(Integer, nullable=False, unique=True)
    nome = Column(String, nullable=False)
    cod_situacao_fiscal = Column(Integer, nullable=False)
    cod_fase_cobranca = Column(Integer, nullable=False)
    cod_exigibilidade = Column(Integer, nullable=False)
    tipo = Column(String, nullable=False)
