from typing import List
from sqlalchemy.orm import Session
from App.DTOs.recuperacaoDTO import RecuperacaoDTO
from App.Models.Recuperacao import Recuperacao
from App.Models.Cda import Cda  # importa o model de CDA
from App.Repositories.Db.Recuperacao.IRecuperacaoRepository import IRecuperacaoRepository

class RecuperacaoRepository(IRecuperacaoRepository):
    def __init__(self, session: Session):
        self.session = session

    def save_all(self, recuperacoes: List[RecuperacaoDTO]) -> None:
        try:
            existing_cdas = {
                cda[0]  
                for cda in self.session.query(Cda.num_cda).all()
            }

            valid_recuperacoes = [
                r for r in recuperacoes if r.num_cda in existing_cdas
            ]

            entities = [
                Recuperacao(
                    num_cda=n.num_cda,
                    prob_recuperacao=n.prob_recuperacao,
                    sts_recuperacao=n.sts_recuperacao
                )
                for n in valid_recuperacoes
            ]

            if entities:  
                self.session.bulk_save_objects(entities)
                self.session.commit()

        except Exception as e:
            self.session.rollback()
            raise e
