from sqlalchemy import Column, Integer, String
from Database.db import Base

class SituacaoCda(Base):
    __tablename__ = "situacao_cdas"

    cod_situacao_cda = Column(Integer, primary_key=True, autoincrement=False)
    nome = Column(String, nullable=False)
    cod_situacao_fiscal = Column(Integer, nullable=False)
    cod_fase_cobranca = Column(Integer, nullable=False)
    cod_exigibilidade = Column(Integer, nullable=False)
    tipo = Column(String, nullable=False)
