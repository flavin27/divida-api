from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from Database.dw import Base
from App.Models.Dw.DimNaturezaDivida import DimNaturezaDivida
from sqlalchemy.orm import relationship
from App.Models.Dw.DimData import DimData
from App.Models.Dw.DimSituacaoCda import DimSituacaoCda




class FactCda(Base):
    __tablename__ = 'fact_cdas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    num_cda = Column(String, nullable=False)
    natureza_id = Column(Integer, ForeignKey('dim_natureza_dividas.id'), nullable=False)
    situacao_id = Column(Integer, ForeignKey('dim_situacao_cdas.id'), nullable=False)
    ano_inscricao_id = Column(Integer, ForeignKey('dim_datas.id'), nullable=False)
    data_situacao_id = Column(Integer, ForeignKey('dim_datas.id'), nullable=False)
    data_cadastramento_id = Column(Integer, ForeignKey('dim_datas.id'), nullable=False)
    cod_fase_cobranca = Column(String, nullable=False)
    valor_saldo = Column(Numeric(15, 2), nullable=False)

    natureza = relationship("DimNaturezaDivida")
    situacao = relationship("DimSituacaoCda")
    ano_inscricao = relationship("DimData", foreign_keys=[ano_inscricao_id])
    data_situacao = relationship("DimData", foreign_keys=[data_situacao_id])
    data_cadastramento = relationship("DimData", foreign_keys=[data_cadastramento_id])

from App.Models.Dw.FactRecuperacao import FactRecuperacao

# Define relacionamento depois que FactRecuperacao foi importado
FactCda.recuperacao = relationship("FactRecuperacao", uselist=False, back_populates="cda")
