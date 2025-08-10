from datetime import datetime
from typing import List
from sqlalchemy import desc, asc
from sqlalchemy.orm import Session, joinedload
from App.DTOs.Dw.dim_dataDTO import DimDataDTO
from App.DTOs.cdaDTO import CdaDTO
from App.Models.Dw.FactCda import FactCda
from App.Repositories.Dw.FactCda.IFactCdaRepository import IFactCdaRepository
from App.Repositories.Dw.DimData.DimDataRepository import DimDataRepository
from App.Repositories.Dw.DimSituacaoCda.DimSituacaoCdaRepository import DimSituacaoCdaRepository
from App.Http.Requests.CdaResquest import CdaRequest

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
        

    def index(self, request: CdaRequest):
        query = (
            self.session.query(FactCda)
            .join(FactCda.natureza)
            .join(FactCda.situacao)
            .join(FactCda.ano_inscricao)
            .outerjoin(FactCda.recuperacao)
            .options(joinedload(FactCda.recuperacao))  # Carregar relacionamento para evitar lazy load
        )

        if request.numCDA:
            query = query.filter(FactCda.num_cda == request.numCDA)
        if request.minSaldo is not None:
            query = query.filter(FactCda.valor_saldo >= request.minSaldo)
        if request.maxSaldo is not None:
            query = query.filter(FactCda.valor_saldo <= request.maxSaldo)
        if request.minAno is not None:
            query = query.filter(FactCda.ano_inscricao.ano >= request.minAno)  
        if request.maxAno is not None:
            query = query.filter(FactCda.ano_inscricao.ano <= request.maxAno)
        if request.natureza:
            query = query.filter(FactCda.natureza.nome == request.natureza)  
        if request.agrupamento_situacao is not None:
            query = query.filter(FactCda.situacao.id == request.agrupamento_situacao)

        if request.sort_by in ("ano", "valor"):
            if request.sort_by == "ano":
                sort_col = FactCda.ano_inscricao.ano
            else:
                sort_col = FactCda.valor_saldo
            if request.sort_order == "desc":
                query = query.order_by(desc(sort_col))
            else:
                query = query.order_by(asc(sort_col))

        results = query.all()

        ano_atual = datetime.now().year

        response = []
        for item in results:
            anos_idade = ano_atual - getattr(item.ano_inscricao, 'ano', ano_atual)
            response.append({
                "numCDA": item.num_cda,
                "valor_saldo_atualizado": float(item.valor_saldo),
                "qtde_anos_idade_cda": anos_idade,
                "agrupamento_situacao": item.situacao_id,
                "natureza": getattr(item.natureza, "nome", ""),
                "score": item.recuperacao.prob_recuperacao if item.recuperacao else None,
            })

        return response
