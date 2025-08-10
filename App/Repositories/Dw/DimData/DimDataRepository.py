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
    
    def save(self, data: DimDataDTO) -> None:
        try:
            entity = DimData(
                data=data.data,
                ano=data.ano,
                mes=data.mes,
                dia=data.dia,
                trimestre=data.trimestre,
                semana=data.semana,
                dia_semana=data.dia_semana,
            )
            self.session.add(entity)
            self.session.commit()

            return entity.id
        except Exception as e:
            self.session.rollback()
            raise e
        
    def get_id_by_data(self, data):
        try:
            entity = self.session.query(DimData).filter(DimData.data == data).first()
            if entity:
                return entity.id
            return None
        except Exception as e:
            self.session.rollback()
            raise e
