from App.Http.Requests.CdaResquest import CdaRequest
from App.Repositories.Dw.FactCda.FactCdaRepository import FactCdaRepository
from Database.dw import SessionLocal


class CdaController:
    def __init__(self):
        pass
    @staticmethod
    def index(request: CdaRequest):
        session = SessionLocal()
        fact_cda_repository = FactCdaRepository(session)
        data = fact_cda_repository.index(request)
        return {"status": "ok", "data": data}