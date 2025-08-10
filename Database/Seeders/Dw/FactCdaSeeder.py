from Database.dw import SessionLocal
from Database.db import SessionLocal as SessionDb
from App.Repositories.Db.Cda.CdaRepository import CdaRepository
from App.Repositories.Dw.FactCda.FactCdaRepository import FactCdaRepository


class FactCdaSeeder:
    def __init__(self, fact_cda_repo, cda_repo):
        self.fact_cda_repo = fact_cda_repo
        self.cda_repo = cda_repo

    def seed_fact_cda(self) -> None:
        cda_list = self.cda_repo.get_all()
        self.fact_cda_repo.save_all(cda_list)

def run():
    print("Seeding fact_cda...\n")
    session = SessionLocal()
    sessionDb = SessionDb()
    try:
        repo = FactCdaRepository(session)  
        cda_repo = CdaRepository(sessionDb)
        seedDb = FactCdaSeeder(repo, cda_repo)
        seedDb.seed_fact_cda()
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
    print("Database from fact_cda seeded successfully.\n")

if __name__ == "__main__":
    run()
