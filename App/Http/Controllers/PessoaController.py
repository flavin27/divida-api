from App.Http.Requests.CdaResquest import CdaRequest
from App.Repositories.Dw.DimPessoa.DimPessoaRepository import DimPessoaRepository
from Database.dw import SessionLocal


class PessoaController:
    def __init__(self):
        pass
    @staticmethod
    def index():
        session = SessionLocal()
        pessoa_repository = DimPessoaRepository(session)

        dtos = pessoa_repository.index()

        data = []
        for dto in dtos:
            data.append({
                "name": dto.nome, 
                "tipo_pessoa": dto.tipo_documento,
                "CPF/CNPJ": dto.documento,
            })

        session.close()
        return {"status": "ok", "data": data}