from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from Database.db import Base

class HistoricoCda(Base):
    __tablename__ = 'historico_cdas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    num_cda = Column(String, nullable=False)
    ano_inscricao = Column(Integer, nullable=False)
    id_natureza_divida = Column(Integer, ForeignKey('natureza_dividas.id'), nullable=False)
    cod_situacao_cda = Column(String, nullable=False)
    data_situacao = Column(Date, nullable=False)
    cod_fase_cobranca = Column(String, nullable=False)
    data_cadastramento = Column(Date, nullable=False)
    valor_saldo = Column(Numeric(15, 2), nullable=False)
