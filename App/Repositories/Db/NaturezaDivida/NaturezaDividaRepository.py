from typing import List
from sqlalchemy.orm import Session
from App.DTOs.naturezaDividaDTO import NaturezaDividaDTO
from App.Models.Db.NaturezaDivida import NaturezaDivida
from App.Repositories.Db.NaturezaDivida.INaturezaDividaRepository import INaturezaDividaRepository

class NaturezaDividaRepository(INaturezaDividaRepository):
    def __init__(self, session: Session):
        self.session = session

    def save_all(self, naturezas: List[NaturezaDividaDTO]) -> None:
        try:
            entities = [
                NaturezaDivida(
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
    def get_all(self) -> List[NaturezaDividaDTO]:
        try:
            naturezas = self.session.query(NaturezaDivida).all()
            return [
                NaturezaDividaDTO(
                    id=n.id,
                    nome=n.nome,
                    descricao=n.descricao
                )
                for n in naturezas
            ]
        except Exception as e:
            raise e
