from sqlalchemy import Column, ForeignKeyConstraint, Integer, String, Float, ForeignKey
from Database.db import Base, engine


class Create_recuperacoes_table(Base):
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


def run():
    print("Criando tabela recuperacao...")
    Base.metadata.create_all(bind=engine, tables=[Create_recuperacoes_table.__table__])
    print("tabela de recuperacoes criada com sucesso.")

if __name__ == "__main__":
    run()