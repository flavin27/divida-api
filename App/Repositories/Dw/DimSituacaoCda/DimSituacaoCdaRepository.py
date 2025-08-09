from typing import List
from sqlalchemy.orm import Session
from App.DTOs.situacaoCdaDTO import SituacaoCdaDTO
from App.Models.Dw.DimSituacaoCda import DimSituacaoCda
from App.Repositories.Dw.DimSituacaoCda.IDimSituacaoCdaRepository import ISituacaoCdaRepository

class DimSituacaoCdaRepository(ISituacaoCdaRepository):
    def __init__(self, session: Session):
        self.session = session

    def save_all(self, situacoes: List[SituacaoCdaDTO]) -> None:
        try:
            entities = [
                DimSituacaoCda(
                    cod_situacao_cda=n.cod_situacao_cda,
                    nome=n.nome,
                    cod_situacao_fiscal=n.cod_situacao_fiscal,
                    cod_fase_cobranca=n.cod_fase_cobranca,
                    cod_exigibilidade=n.cod_exigibilidade,
                    tipo=n.tipo
                )
                for n in situacoes
            ]
            self.session.bulk_save_objects(entities)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
