from sqlalchemy import Column, String, Integer, Numeric, ForeignKey
from Database.dw import Base, engine

class Create_fact_cdas_table(Base):
    __tablename__ = 'fact_cdas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    num_cda = Column(String, nullable=False)
    natureza_id = Column(Integer, ForeignKey('dim_natureza_dividas.id'), nullable=False)
    situacao_id = Column(Integer, ForeignKey('dim_situacao_cdas.id'), nullable=False)
    ano_inscricao_id = Column(Integer, ForeignKey('dim_datas.id'), nullable=False)
    data_situacao_id = Column(Integer, ForeignKey('dim_datas.id'), nullable=False)
    data_cadastramento_id = Column(Integer, ForeignKey('dim_datas.id'), nullable=False)
    cod_fase_cobranca = Column(String, nullable=False)
    valor_saldo = Column(Numeric(15, 2), nullable=False)

def run():
    print("Criando tabela 'fact_cdas'...")
    Base.metadata.create_all(engine, tables=[Create_fact_cdas_table.__table__])
    print("Tabela 'fact_cdas' criada com sucesso!")

if __name__ == "__main__":
    run()
