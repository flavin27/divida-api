from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from Database.db import Base

class Cda(Base):
    __tablename__ = 'cdas'

    num_cda = Column(String, primary_key=True, unique=True, nullable=False)
    ano_inscricao = Column(Integer, primary_key=True)
    id_natureza_divida = Column(Integer, ForeignKey('natureza_dividas.id'), nullable=False)
    cod_situacao_cda = Column(String, nullable=False)
    data_situacao = Column(Date, nullable=False)
    cod_fase_cobranca = Column(String, nullable=False)
    data_cadastramento = Column(Date, nullable=False)
    valor_saldo = Column(Numeric(15, 2), nullable=False)
