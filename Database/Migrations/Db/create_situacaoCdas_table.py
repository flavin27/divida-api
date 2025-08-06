from Database.db import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey


class Create_situacaoCdas_able(Base):
    __tablename__ = 'situacao_cdas'

    cod_situacao_cda = Column(Integer, primary_key=True, autoincrement=False)
    nome = Column(String, nullable=False)
    cod_situacao_fiscal = Column(Integer, nullable=False)
    cod_fase_cobranca = Column(Integer, nullable=False)
    cod_exigibilidade = Column(Integer, nullable=False)
    tipo = Column(String, nullable=False)


def run():
    print("Criando tabela 'situacao_cdas'...")
    Base.metadata.create_all(engine, tables=[Create_situacaoCdas_able.__table__])
    print("Tabela 'situacao_cdas' criada com sucesso!")

if __name__ == "__main__":
    run()
