from sqlalchemy import Column, String, Integer, ForeignKey
from Database.dw import Base, engine

class Create_fact_cdas_pessoas_table(Base):

    __tablename__ = 'fact_cdas_pessoas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cda_id = Column(Integer, ForeignKey('fact_cdas.id'), nullable=False)
    pessoa_id = Column(Integer, ForeignKey('dim_pessoas.id'), nullable=False)
    sitacao_devedor = Column(String, nullable=False)

def run():
    print("Criando tabela 'fact_cdas_pessoas'...")
    Base.metadata.create_all(engine, tables=[Create_fact_cdas_pessoas_table.__table__])
    print("Tabela 'fact_cdas_pessoas' criada com sucesso!")

if __name__ == "__main__":
    run()
