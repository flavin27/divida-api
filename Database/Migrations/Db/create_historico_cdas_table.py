from sqlalchemy import Column, String, Integer, Numeric, Date, ForeignKey, UniqueConstraint
from Database.db import Base, engine

class Create_historico_cdas_tables(Base):
    __tablename__ = 'historico_cdas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    num_cda = Column(String, nullable=False)
    ano_inscricao = Column(Integer, nullable=False)
    id_natureza_divida = Column(Integer, ForeignKey('natureza_dividas.id'), nullable=False)
    cod_situacao_cda = Column(Integer, ForeignKey('situacao_cdas.cod_situacao_cda'), nullable=False)
    data_situacao = Column(Date, nullable=False)
    cod_fase_cobranca = Column(String, nullable=False)
    data_cadastramento = Column(Date, nullable=False)
    valor_saldo = Column(Numeric(15, 2), nullable=False)


def run():
    print("Criando tabela 'historico_cdas'...")
    Base.metadata.create_all(engine, tables=[Create_historico_cdas_tables.__table__])
    print("Tabela 'historico_cdas' criada com sucesso!")

if __name__ == "__main__":
    run()
