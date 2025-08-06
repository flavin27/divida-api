from Database.db import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey, Table, PrimaryKeyConstraint, ForeignKeyConstraint


class Create_cdas_pessoas_table(Base):
    __tablename__ = 'cdas_pessoas'

    num_cda = Column(String, primary_key=True)
    ano_inscricao = Column(Integer, primary_key=True)
    id_pessoa = Column(Integer, primary_key=True)

    __table_args__ = (
        ForeignKeyConstraint(
            ['num_cda', 'ano_inscricao'],
            ['cdas.num_cda', 'cdas.ano_inscricao']
        ),
        ForeignKeyConstraint(['id_pessoa'], ['pessoas.id']),
    )


def run():
    print("Criando tabela cdas_pessoas (pivot)...")
    Base.metadata.create_all(bind=engine, tables=[Create_cdas_pessoas_table.__table__])
    print("Tabela criada com sucesso.")

if __name__ == "__main__":
    run()
