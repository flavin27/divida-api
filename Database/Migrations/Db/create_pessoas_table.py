from sqlalchemy import Column, String, Integer, Numeric, Date, ForeignKey
from Database.db import Base, engine
from sqlalchemy.types import Enum as SqlEnum 
from App.Enums.DocumentEnum import DocumentEnum


class Create_pessoas_tables(Base):
    __tablename__ = 'pessoas'

    id = Column(Integer, primary_key=True, autoincrement=False)
    nome = Column(String, nullable=False)
    documento = Column(String, nullable=True)
    tipo_documento = Column(SqlEnum(DocumentEnum), nullable=False)

def run():
    print("Criando tabela 'pessoas'...")
    Base.metadata.create_all(engine, tables=[Create_pessoas_tables.__table__])
    print("Tabela 'pessoas' criada com sucesso!")

if __name__ == "__main__":
    run()
