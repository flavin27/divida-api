from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from Database.dw import Base

class FactCda(Base):
    __tablename__ = 'fact_cdas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    num_cda = Column(String, nullable=False)
    natureza_id = Column(Integer, ForeignKey('dim_natureza_dividas.id'), nullable=False)
    situacao_id = Column(Integer, ForeignKey('dim_situacao_cdas.id'), nullable=False)
    data_situacao_id = Column(Integer, ForeignKey('dim_datas.id'), nullable=False)
    data_cadastramento_id = Column(Integer, ForeignKey('dim_datas.id'), nullable=False)
    cod_fase_cobranca = Column(String, nullable=False)
    valor_saldo = Column(Numeric(15, 2), nullable=False)
