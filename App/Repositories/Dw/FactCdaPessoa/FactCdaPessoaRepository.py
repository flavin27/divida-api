from sqlalchemy.orm import Session
from typing import List
from App.DTOs.cda_pessoaDTO import CdaPessoaDTO
from App.Models.Dw.FactCdaPessoa import FactCdaPessoa
from App.Repositories.Dw.DimPessoa.DimPessoaRepository import DimPessoaRepository
from App.Repositories.Dw.FactCda.FactCdaRepository import FactCdaRepository


class FactCdaPessoaRepository:
    def __init__(self, session: Session):
        self.session = session

    def save_all(self, cdasPessoas: List[CdaPessoaDTO]) -> None:
        try:
            dim_pessoas_repo = DimPessoaRepository(self.session)
            fact_cdas_repo = FactCdaRepository(self.session)

            fact_cdas_list = fact_cdas_repo.get_all()
            dim_pessoas_list = dim_pessoas_repo.get_all()

        




            entities = [
                FactCdaPessoa(
                    cda_id = fact_cdas_list.get(n.num_cda),
                    pessoa_id = dim_pessoas_list.get(str(n.idPessoa)),
                    sitacao_devedor = n.sitacao_devedor
                )
                for n in cdasPessoas
            ]
            self.session.bulk_save_objects(entities)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        
