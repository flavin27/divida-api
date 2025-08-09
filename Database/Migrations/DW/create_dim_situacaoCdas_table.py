from Database.dw import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey


class Create_dim_situacaoCdas_table(Base):

    __tablename__ = 'dim_situacao_cdas'

    id = Column(Integer, primary_key=True, autoincrement=True)  
    cod_situacao_cda = Column(Integer, nullable=False, unique=True)      
    nome = Column(String, nullable=False)
    cod_situacao_fiscal = Column(Integer, nullable=False)
    cod_fase_cobranca = Column(Integer, nullable=False)
    cod_exigibilidade = Column(Integer, nullable=False)
    tipo = Column(String, nullable=False)


def run():
    print("Criando tabela 'dim_situacao_cdas'...")
    Base.metadata.create_all(engine, tables=[Create_dim_situacaoCdas_table.__table__])
    print("Tabela 'dim_situacao_cdas' criada com sucesso!")

if __name__ == "__main__":
    run()
