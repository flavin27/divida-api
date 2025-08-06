from sqlalchemy import Column, String, Integer, Numeric, Date, ForeignKey
from Database.db import Base, engine

class Create_naturezaDividas_table(Base):
    __tablename__ = 'natureza_dividas'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    descricao = Column(String)

def run():
    print("Criando tabela 'naturezas'...")
    Base.metadata.create_all(engine, tables=[Create_naturezaDividas_table.__table__])
    print("Tabela 'naturezas' criada com sucesso!")

if __name__ == "__main__":
    run()
