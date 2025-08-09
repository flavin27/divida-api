from sqlalchemy import Column, Date, Integer, String
from Database.dw import Base

class DimData(Base):
    __tablename__ = "dim_datas"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(Date, nullable=False, unique=True)
    ano = Column(Integer, nullable=False)
    mes = Column(Integer, nullable=False)
    dia = Column(Integer, nullable=False)
    trimestre = Column(Integer, nullable=False)
    semana = Column(Integer, nullable=False)
    dia_semana = Column(Integer, nullable=False)
