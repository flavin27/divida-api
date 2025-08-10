from sqlalchemy import Column, Integer, String, Float, ForeignKeyConstraint, ForeignKey
from Database.dw import Base
from sqlalchemy.types import Enum as SqlEnum 
from App.Models.Dw.FactCda import FactCda

class FactRecuperacao(Base):
    __tablename__ = 'fact_recuperacoes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    num_cda = Column(String, nullable=False)
    prob_recuperacao = Column(Float, nullable=False)
    sts_recuperacao = Column(String, nullable=False)
    cda_id = Column(Integer, ForeignKey('fact_cdas.id'), nullable=False)


    __table_args__ = (
        ForeignKeyConstraint(
            ['cda_id'], ['fact_cdas.id'],
            onupdate="CASCADE", ondelete="CASCADE"
        ),
    )


