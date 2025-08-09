from typing import List
from sqlalchemy.orm import Session
from App.DTOs.naturezaDividaDTO import NaturezaDividaDTO
from App.Models.Dw.DimNaturezaDivida import DimNaturezaDivida
from App.Repositories.Dw.DimNaturezaDivida.IDimNaturezaDividaRepository import IDimNaturezaDividaRepository

class DimNaturezaDividaRepository(IDimNaturezaDividaRepository):
    def __init__(self, session: Session):
        self.session = session

    def save_all(self, naturezas: List[NaturezaDividaDTO]) -> None:
        try:
            entities = [
                DimNaturezaDivida(
                    id=n.id,
                    nome=n.nome,
                    descricao=n.descricao
                )
                for n in naturezas
            ]
            self.session.bulk_save_objects(entities)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
