from sqlalchemy import Column, String, Integer, Float, ForeignKey
from Database.dw import Base, engine

class Create_fact_recuperacoes_table(Base):

    __tablename__ = 'fact_recuperacoes'

    recuperacao_key = Column(Integer, primary_key=True, autoincrement=True)
    num_cda = Column(String, nullable=False)
    prob_recuperacao = Column(Float, nullable=False)
    sts_recuperacao = Column(String, nullable=False)
    cda_id = Column(Integer, ForeignKey('fact_cdas.id'), nullable=False)

def run():
    print("Criando tabela 'fact_recuperacoes'...")
    Base.metadata.create_all(engine, tables=[Create_fact_recuperacoes_table.__table__])
    print("Tabela 'fact_recuperacoes' criada com sucesso!")

if __name__ == "__main__":
    run()
