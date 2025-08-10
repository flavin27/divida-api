from typing import List
from sqlalchemy.orm import Session
from App.DTOs.recuperacaoDTO import RecuperacaoDTO
from App.Models.Dw.FactRecuperacao import FactRecuperacao
from App.Models.Dw.FactCda import FactCda
from App.Repositories.Dw.FactCda.FactCdaRepository import FactCdaRepository
from App.Repositories.Dw.FactRecuperacao.IFactRecuperacaoRepository import IFactRecuperacaoRepository

class FactRecuperacaoRepository(IFactRecuperacaoRepository):
    def __init__(self, session: Session):
        self.session = session

    def save_all(self, recuperacoes: List[RecuperacaoDTO]) -> None:
        try:
            fact_cda_repo = FactCdaRepository(self.session)
            existing_cdas = fact_cda_repo.get_all()



            valid_recuperacoes = [
                r for r in recuperacoes if r.num_cda in existing_cdas.keys()
            ]

            entities = [
                FactRecuperacao(
                    num_cda=n.num_cda,
                    prob_recuperacao=n.prob_recuperacao,
                    sts_recuperacao=n.sts_recuperacao,
                    cda_id=existing_cdas.get(n.num_cda)
                )
                for n in valid_recuperacoes
            ]

            if entities:  
                self.session.bulk_save_objects(entities)
                self.session.commit()

        except Exception as e:
            self.session.rollback()
            raise e
                # Salva todas as recuperacoes na base de dados
