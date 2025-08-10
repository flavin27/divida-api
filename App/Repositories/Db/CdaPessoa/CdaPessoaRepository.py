from typing import List
from sqlalchemy.orm import Session
from App.DTOs.cda_pessoaDTO import CdaPessoaDTO
from App.Models.Db.CdaPessoa import CdaPessoa
from App.Models.Db.Cda import Cda
from App.Models.Db.Pessoa import Pessoa
from App.Repositories.Db.CdaPessoa.ICdaPessoaRepository import ICdaPessoaRepository

class CdaPessoaRepository(ICdaPessoaRepository):
    def __init__(self, session: Session):
        self.session = session

    def save_all(self, cdas: List[CdaPessoaDTO]) -> None:
        try:
            existing_cdas = {
                cda[0] for cda in self.session.query(Cda.num_cda).all()
            }

            existing_pessoas = {
                pessoa[0] for pessoa in self.session.query(Pessoa.id).all()
            }

            valid_cdas = [
                r for r in cdas
                if r.num_cda in existing_cdas and r.idPessoa in existing_pessoas
            ]

            entities = [
                CdaPessoa(
                    num_cda=n.num_cda,
                    id_pessoa=n.idPessoa,
                    sitacao_devedor=n.sitacao_devedor
                )
                for n in valid_cdas
            ]

            if entities: 
                self.session.bulk_save_objects(entities)
                self.session.commit()

        except Exception as e:
            self.session.rollback()
            raise e

    def get_all(self) -> List[CdaPessoaDTO]:
        try:
            cda_pessoa_list = self.session.query(CdaPessoa).all()
            return [CdaPessoaDTO(
                num_cda=n.num_cda,
                idPessoa=n.id_pessoa,
                sitacao_devedor=n.sitacao_devedor
            )                 
            for n in cda_pessoa_list]
        except Exception as e:
            self.session.rollback()
            raise e
    
    def get_all_with_document(self) -> List[CdaPessoaDTO]:
        try:
            results = (
                self.session.query(
                    CdaPessoa.num_cda,
                    Pessoa.documento,
                    CdaPessoa.sitacao_devedor
                )
                .join(Pessoa, CdaPessoa.id_pessoa == Pessoa.id)
                .all()
            )

            return [
                CdaPessoaDTO(
                    num_cda=num_cda,
                    idPessoa=documento,  
                    sitacao_devedor=sitacao_devedor
                )
                for num_cda, documento, sitacao_devedor in results
            ]
        except Exception as e:
            self.session.rollback()
            raise e
