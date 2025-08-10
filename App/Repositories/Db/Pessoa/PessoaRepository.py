from typing import List
from sqlalchemy.orm import Session
from App.DTOs.pessoaDTO import PessoaDTO
from App.Models.Db.Pessoa import Pessoa
from App.Repositories.Db.Pessoa.IPessoaRepository import IPessoaRepository

class PessoaRepository(IPessoaRepository):
    def __init__(self, session: Session):
        self.session = session

    def save_all(self, pessoas: List[PessoaDTO]) -> None:
        try:
            entities = [
                Pessoa(
                    id = n.id,
                    nome = n.nome,
                    documento = n.documento,
                    tipo_documento = n.tipo_documento,
                )
                for n in pessoas
            ]
            self.session.bulk_save_objects(entities)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

    def get_all(self) -> List[PessoaDTO]:
        try:
            pessoas = self.session.query(Pessoa).all()
            return [
                PessoaDTO(
                    id=n.id,
                    nome=n.nome,
                    documento=n.documento,
                    tipo_documento=n.tipo_documento,
                )
                for n in pessoas
            ]
        except Exception as e:
            raise e

    def get_all_as_map(self):
        try:
            pessoa_list = self.session.query(Pessoa.id, Pessoa.documento).all()

            return {documento: id for id, documento in pessoa_list}
        except Exception as e:
            self.session.rollback()
            raise e