from sqlalchemy import Column, Integer, String, Float, ForeignKeyConstraint
from Database.db import Base
from sqlalchemy.types import Enum as SqlEnum 

class Recuperacao(Base):
    __tablename__ = "recuperacoes"

    num_cda = Column(String, primary_key=True)

    prob_recuperacao = Column(Float, nullable=False)
    sts_recuperacao = Column(String, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(
            ['num_cda'],
            ['cdas.num_cda'],
            name='fk_recuperacoes_num_cda',
            ondelete='CASCADE',
        ),
    )


