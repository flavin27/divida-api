from sqlalchemy import Column, String, Integer
from Database.dw import Base, engine
from sqlalchemy.types import Enum as SqlEnum
from App.Enums.DocumentEnum import DocumentEnum

class Create_dim_pessoas_table(Base):
    __tablename__ = 'dim_pessoas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    documento = Column(String, nullable=True)
    tipo_documento = Column(SqlEnum(DocumentEnum), nullable=False)

def run():
    print("Criando tabela 'dim_pessoas'...")
    Base.metadata.create_all(engine, tables=[Create_dim_pessoas_table.__table__])
    print("Tabela 'dim_pessoas' criada com sucesso!")

if __name__ == "__main__":
    run()
