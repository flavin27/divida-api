from datetime import datetime
from typing import List
from sqlalchemy.orm import Session
from App.DTOs.Dw.dim_dataDTO import DimDataDTO
from App.DTOs.cdaDTO import CdaDTO
from App.Models.Dw.FactCda import FactCda
from App.Repositories.Dw.FactCda.IFactCdaRepository import IFactCdaRepository
from App.Repositories.Dw.DimData.DimDataRepository import DimDataRepository
from App.Repositories.Dw.DimSituacaoCda.DimSituacaoCdaRepository import DimSituacaoCdaRepository

class FactCdaRepository(IFactCdaRepository):
    def __init__(self, session: Session):
        self.session = session

    def save_all(self, situacoes: List[CdaDTO]) -> None:
        try:
            dim_data_repo = DimDataRepository(self.session)
            situacao_repo = DimSituacaoCdaRepository(self.session)
            entities = []

            for n in situacoes:
                ano_inscricao_data = datetime(n.ano_inscricao, 1, 1)

                ano_inscricao_id = dim_data_repo.get_id_by_data(ano_inscricao_data)
                if not ano_inscricao_id:
                    ano_inscricao_id = dim_data_repo.save(
                        DimDataDTO(
                            data=ano_inscricao_data,
                            ano=n.ano_inscricao,
                            mes=1,
                            dia=1,
                            trimestre=1,
                            semana=1,
                            dia_semana=6  
                        )
                    )

                data_situacao_id = None
                if n.data_situacao:
                    data_situacao_id = dim_data_repo.get_id_by_data(n.data_situacao)
                    if not data_situacao_id:
                        data_situacao_id = dim_data_repo.save(self._build_dim_data_dto(n.data_situacao))

                data_cadastramento_id = None
                if n.data_cadastramento:
                    data_cadastramento_id = dim_data_repo.get_id_by_data(n.data_cadastramento)
                    if not data_cadastramento_id:
                        data_cadastramento_id = dim_data_repo.save(self._build_dim_data_dto(n.data_cadastramento))

                situacao_id = situacao_repo.get_id_by_cod_situacao(n.cod_situacao_cda)

                

                entities.append(
                    FactCda(
                        num_cda=n.num_cda,
                        natureza_id=n.id_natureza_divida,
                        ano_inscricao_id=ano_inscricao_id,
                        situacao_id=situacao_id,
                        data_situacao_id=data_situacao_id,
                        data_cadastramento_id=data_cadastramento_id,
                        cod_fase_cobranca=n.cod_fase_cobranca,
                        valor_saldo=n.valor_saldo
                    )
                )

            self.session.bulk_save_objects(entities)
            self.session.commit()

        except Exception as e:
            self.session.rollback()
            raise e

    def _build_dim_data_dto(self, data: datetime) -> DimDataDTO:
        return DimDataDTO(
            data=data,
            ano=data.year,
            mes=data.month,
            dia=data.day,
            trimestre=((data.month - 1) // 3) + 1,
            semana=data.isocalendar()[1],
            dia_semana=data.weekday()
        )
    

    def get_all(self):
        try:
            fact_cda_list = self.session.query(FactCda.id, FactCda.num_cda).all()

            return {num_cda: id for id, num_cda in fact_cda_list}
        except Exception as e:
            self.session.rollback()
            raise e


    def get_id_by_cda(self, cda):
        try:
            entity = self.session.query(FactCda).filter(FactCda.num_cda == cda).first()
            if entity:
                return entity.id
            return None
        except Exception as e:
            self.session.rollback()
            raise e
