from Database.dw import SessionLocal
from Database.db import SessionLocal as SessionDb
from App.Repositories.Db.SituacaoCda.SituacaoCdaRepository import SituacaoCdaRepository
from App.Repositories.Dw.DimSituacaoCda.DimSituacaoCdaRepository import DimSituacaoCdaRepository


class DimSituacaoCdaSeeder:
    def __init__(self, dim_situacao_cda_repo, situacao_cda_repo):
        self.dim_situacao_cda_repo = dim_situacao_cda_repo
        self.situacao_cda_repo = situacao_cda_repo

    def seed_dim_situacao_cda(self) -> None:
        dim_situacao_cda_list = self.situacao_cda_repo.get_all()
        self.dim_situacao_cda_repo.save_all(dim_situacao_cda_list)

def run():
    print("Seeding dim situacao cda...\n")
    session = SessionLocal()
    sessionDb = SessionDb()
    try:
        repo = DimSituacaoCdaRepository(session)  
        situacao_cda_repo = SituacaoCdaRepository(sessionDb)
        seedDb = DimSituacaoCdaSeeder(repo, situacao_cda_repo)
        seedDb.seed_dim_situacao_cda()
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
    print("Database from dim_situacao_cda seeded successfully.\n")

if __name__ == "__main__":
    run()
