from sqlalchemy import Column, Integer, String, ForeignKey, ForeignKeyConstraint
from Database.db import Base

class CdaPessoa(Base):
    __tablename__ = 'cdas_pessoas'

    num_cda = Column(String, primary_key=True)
    id_pessoa = Column(Integer, primary_key=True)
    sitacao_devedor = Column(String, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(
            ['num_cda'],
            ['cdas.num_cda'],
            name='fk_cdas_pessoas_num_cda',
            ondelete='CASCADE',
        ),
        ForeignKeyConstraint(['id_pessoa'], ['pessoas.id']),
    )
