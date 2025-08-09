from typing import List
from sqlalchemy.orm import Session
from App.DTOs.Dw.dim_dataDTO import DimDataDTO
from App.Models.Dw.DimData import DimData
from App.Repositories.Dw.DimData.IDimDataRepository import IDimDataRepository

class DimDataRepository(IDimDataRepository):
    def __init__(self, session: Session):
        self.session = session

    def save_all(self, datas: List[DimDataDTO]) -> None:
        try:
            entities = [
                DimData(
                    data =n.data,
                    ano =n.ano,
                    mes =n.mes,
                    dia =n.dia,
                    trimestre =n.trimestre,
                    semana =n.semana,
                    dia_semana =n.dia_semana,
                )
                for n in datas
            ]
            self.session.bulk_save_objects(entities)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
