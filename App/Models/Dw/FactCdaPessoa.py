from sqlalchemy import Column, Integer, String, ForeignKey, ForeignKeyConstraint
from Database.dw import Base

class FactCdaPessoa(Base):
    __tablename__ = 'fact_cdas_pessoas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cda_id = Column(Integer, ForeignKey('fact_cdas.id'), nullable=False)
    pessoa_id = Column(Integer, ForeignKey('dim_pessoas.id'), nullable=False)
    sitacao_devedor = Column(String, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(
            ['cda_id'],
            ['fact_cdas.num_cda'],
            name='fk_cdas_pessoas_num_cda',
            ondelete='CASCADE',
        ),
        ForeignKeyConstraint(['pessoa_id'], ['dim_pessoas.id']),
    )
