from sqlalchemy import Column, Integer, Date
from Database.dw import Base, engine

class Create_dim_datas_table(Base):
    __tablename__ = 'dim_datas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(Date, nullable=False, unique=True)
    ano = Column(Integer, nullable=False)
    mes = Column(Integer, nullable=False)
    dia = Column(Integer, nullable=False)
    trimestre = Column(Integer, nullable=False)
    semana = Column(Integer, nullable=False)
    dia_semana = Column(Integer, nullable=False)

def run():
    print("Criando tabela 'dim_datas'...")
    Base.metadata.create_all(engine, tables=[Create_dim_datas_table.__table__])
    print("Tabela 'dim_datas' criada com sucesso!")

if __name__ == "__main__":
    run()
