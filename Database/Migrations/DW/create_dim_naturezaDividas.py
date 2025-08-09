from sqlalchemy import Column, String, Integer
from Database.dw import Base, engine

class Create_dim_naturezaDividas_table(Base):
    __tablename__ = 'dim_natureza_dividas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=True)

def run():
    print("Criando tabela 'dim_natureza_dividas'...")
    Base.metadata.create_all(engine, tables=[Create_dim_naturezaDividas_table.__table__])
    print("Tabela 'dim_natureza_dividas' criada com sucesso!")

if __name__ == "__main__":
    run()
