from sqlalchemy import Column, String, Integer, Numeric, Date, ForeignKey, UniqueConstraint
from Database.db import Base, engine

class Create_cdas_tables(Base):
    __tablename__ = 'cdas'

    num_cda = Column(String, primary_key=True)
    ano_inscricao = Column(Integer, primary_key=True)
    id_natureza_divida = Column(Integer, ForeignKey('natureza_dividas.id'), nullable=False)
    cod_fase_cobranca = Column(String, nullable=False)
    data_cadastramento = Column(Date, nullable=False)
    valor_saldo = Column(Numeric(15, 2), nullable=False)

    __table_args__ = (
        UniqueConstraint('num_cda'),  # ← Aqui é onde garantimos que num_cda seja único
    )

def run():
    print("Criando tabela 'cdas'...")
    Base.metadata.create_all(engine, tables=[Create_cdas_tables.__table__])
    print("Tabela 'cdas' criada com sucesso!")

if __name__ == "__main__":
    run()
