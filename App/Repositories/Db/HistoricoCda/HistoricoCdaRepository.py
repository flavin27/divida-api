from typing import List
from sqlalchemy.orm import Session
from App.DTOs.cdaDTO import CdaDTO
from App.Models.HistoricoCda import HistoricoCda
from App.Repositories.Db.HistoricoCda.IHistoricoCdaRepository import IHistoricoCdaRepository
from App.Models.NaturezaDivida import NaturezaDivida

class HistoricoCdaRepository(IHistoricoCdaRepository):
    def __init__(self, session: Session):
        self.session = session

    def save_all(self, cdas: List[CdaDTO]) -> None:
        try:
            entities = [
                HistoricoCda(
                    num_cda = n.num_cda,
                    ano_inscricao = n.ano_inscricao,
                    id_natureza_divida = n.id_natureza_divida,
                    cod_situacao_cda = n.cod_situacao_cda,
                    data_situacao = n.data_situacao,
                    data_cadastramento = n.data_cadastramento,
                    cod_fase_cobranca = n.cod_fase_cobranca,
                    valor_saldo = n.valor_saldo,
                )
                for n in cdas
            ]
            self.session.bulk_save_objects(entities)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
