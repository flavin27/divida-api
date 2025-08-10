from typing import List
from sqlalchemy.orm import Session
from App.DTOs.pessoaDTO import PessoaDTO
from App.Models.Dw.DimPessoa import DimPessoa
from App.Repositories.Dw.DimPessoa.IDimPessoaRepository import IDimPessoaRepository

class DimPessoaRepository(IDimPessoaRepository):
    def __init__(self, session: Session):
        self.session = session

    def save_all(self, pessoas: List[PessoaDTO]) -> None:
        try:
            entities = [
                DimPessoa(
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

    def get_all(self):
        try:
            pessoa_list = self.session.query(DimPessoa.id, DimPessoa.documento).all()

            return {documento: id for id, documento in pessoa_list}
        except Exception as e:
            self.session.rollback()
            raise e
    
    def index(self) -> List[PessoaDTO]:
        try:
            pessoas = self.session.query(DimPessoa).all()
            lista_dtos = []
            for p in pessoas:
                dto = PessoaDTO(
                    id=p.id,
                    nome=p.nome,
                    documento = p.documento,
                    tipo_documento = p.tipo_documento
                    
                )
                lista_dtos.append(dto)
            return lista_dtos
        except Exception as e:
            self.session.rollback()
            raise e