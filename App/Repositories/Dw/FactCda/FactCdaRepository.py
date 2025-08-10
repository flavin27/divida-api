from datetime import datetime
from typing import List
from sqlalchemy import case, desc, asc, func
from sqlalchemy.orm import Session, joinedload
from App.DTOs.Dw.dim_dataDTO import DimDataDTO
from App.DTOs.cdaDTO import CdaDTO
from App.Models.Dw.DimNaturezaDivida import DimNaturezaDivida
from App.Models.Dw.DimSituacaoCda import DimSituacaoCda
from App.Models.Dw.FactCda import FactCda
from App.Repositories.Dw.FactCda.IFactCdaRepository import IFactCdaRepository
from App.Repositories.Dw.DimData.DimDataRepository import DimDataRepository
from App.Repositories.Dw.DimSituacaoCda.DimSituacaoCdaRepository import DimSituacaoCdaRepository
from App.Http.Requests.CdaResquest import CdaRequest
from App.Models.Dw.DimData import DimData

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
    
    def get_distribuicao_cdas(self):
        results = (
            self.session.query(
                DimNaturezaDivida.nome.label("natureza"),
                DimSituacaoCda.nome.label("situacao"),
                func.sum(FactCda.valor_saldo).label("total_saldo")
            )
            .join(FactCda.natureza)
            .join(FactCda.situacao)
            .group_by(DimNaturezaDivida.nome, DimSituacaoCda.nome)
            .all()
        )

        temp = {}
        for natureza, situacao, total in results:
            if natureza not in temp:
                temp[natureza] = {}
            temp[natureza][situacao] = float(total)

        lista_formatada = []
        for natureza, situacoes in temp.items():
            total_geral = sum(situacoes.values()) or 1  
            lista_formatada.append({
                "name": natureza,
                "Em cobranca": round(((situacoes.get("Cobrança", 0.0) + situacoes.get("Cobrança Garantida", 0.0) )/ total_geral) * 100, 2),
                "Cancelada": round((situacoes.get("Cancelada", 0.0) / total_geral) * 100, 2),
                "Quitada": round(((situacoes.get("Paga", 0.0) +situacoes.get("Paga por Guia Especial", 0.0)  + situacoes.get("Paga por Conversão", 0.0)) / total_geral) * 100, 2)
            })

        return lista_formatada
    
    def get_inscricoes(self):
        try:
            results = (
                self.session.query(
                    DimData.ano.label("ano"),
                    func.count(FactCda.id).label("Quantidade")
                )
                .join(FactCda.ano_inscricao)
                .group_by(DimData.ano)
                .order_by(DimData.ano)
                .all()
            )
            return [{"ano": ano, "Quantidade": quantidade} for ano, quantidade in results]

        except Exception as e:
            self.session.rollback()
            raise e
        
    def get_montante(self):
        try:
            percentis = [1, 5, 10, 25, 50, 75, 90, 95, 99]
            response = []

            totais = dict(
                self.session.query(
                    DimNaturezaDivida.nome,
                    func.coalesce(func.sum(FactCda.valor_saldo), 0)
                )
                .join(FactCda.natureza)
                .group_by(DimNaturezaDivida.nome)
                .all()
            )

            for p in percentis:
                subquery = (
                    self.session.query(
                        FactCda.natureza_id.label('natureza_id'),
                        func.percentile_cont(p / 100.0).within_group(FactCda.valor_saldo).label('valor_percentil')
                    )
                    .group_by(FactCda.natureza_id)
                    .subquery()
                )

                query = (
                    self.session.query(
                        DimNaturezaDivida.nome.label('natureza'),
                        func.coalesce(func.sum(FactCda.valor_saldo), 0).label('acumulado')
                    )
                    .join(DimNaturezaDivida, FactCda.natureza_id == DimNaturezaDivida.id)
                    .join(subquery, FactCda.natureza_id == subquery.c.natureza_id)
                    .filter(FactCda.valor_saldo <= subquery.c.valor_percentil)
                    .group_by(DimNaturezaDivida.nome)
                )

                resultados = query.all()

                registro = {'Percentual': p}
                for natureza in totais.keys():
                    registro[natureza] = 0.0

                for natureza, acumulado in resultados:
                    total_geral = totais.get(natureza, 1) or 1  
                    percentual = (float(acumulado) / float(total_geral)) * 100
                    registro[natureza] = percentual

                response.append(registro)

            return response

        except Exception as e:
            self.session.rollback()
            raise e
        
    def get_natureza(self):
        categoria_case = case(
            (
                DimNaturezaDivida.nome.op('~*')('multa'), 'Multas'
            ),
            (
                DimNaturezaDivida.nome.op('~*')('IPTU'), 'IPTU'
            ),
            (
                DimNaturezaDivida.nome.op('~*')('ISS'), 'ISS'
            ),
            (
                DimNaturezaDivida.nome.op('~*')('Taxa'), 'Taxas'
            ),
            (
                DimNaturezaDivida.nome.op('~*')('ITBI'), 'ITBI'
            ),
            else_='Outros'
        ).label("grupo")

        query = (
            self.session.query(
                categoria_case,
                func.count(FactCda.id).label("Quantidade")
            )
            .join(FactCda.natureza)
            .group_by(categoria_case)
            .order_by(func.count(FactCda.id).desc())
        )

        results = query.all()

        return [{"name": grupo, "Quantidade": qtd} for grupo, qtd in results]
    
    def get_saldo(self):
        categoria_case = case(
            (
                DimNaturezaDivida.nome.op('~*')('multa'), 'Multas'
            ),
            (
                DimNaturezaDivida.nome.op('~*')('IPTU'), 'IPTU'
            ),
            (
                DimNaturezaDivida.nome.op('~*')('ISS'), 'ISS'
            ),
            (
                DimNaturezaDivida.nome.op('~*')('Taxa'), 'Taxas'
            ),
            (
                DimNaturezaDivida.nome.op('~*')('ITBI'), 'ITBI'
            ),
            else_='Outros'
        ).label("grupo")

        results = (
            self.session.query(
                categoria_case,
                func.sum(FactCda.valor_saldo).label("Saldo")
            )
            .join(FactCda.natureza)
            .group_by(categoria_case)
            .all()
        )

        return [
            {
                "name": grupo,
                "Saldo": float(saldo) if saldo is not None else 0.0
            }
            for grupo, saldo in results
        ]