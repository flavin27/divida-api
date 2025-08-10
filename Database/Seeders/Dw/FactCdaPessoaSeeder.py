from Database.dw import SessionLocal
from Database.db import SessionLocal as SessionDb
from App.Repositories.Db.CdaPessoa.CdaPessoaRepository import CdaPessoaRepository
from App.Repositories.Dw.FactCdaPessoa.FactCdaPessoaRepository import FactCdaPessoaRepository


class FactCdaPessoaSeeder:
    def __init__(self, fact_cda_pessoa_repo, cda_pessoa_repo):
        self.fact_cda_pessoa_repo = fact_cda_pessoa_repo
        self.cda_pessoa_repo = cda_pessoa_repo

    def seed_fact_cda_pessoa(self) -> None:
        cda_pessoa_list = self.cda_pessoa_repo.get_all_with_document()
        self.fact_cda_pessoa_repo.save_all(cda_pessoa_list)

def run():
    print("Seeding fact_cda_pessoas...\n")
    session = SessionLocal()
    sessionDb = SessionDb()
    try:
        repo = FactCdaPessoaRepository(session)  
        cda_pessoa_repo = CdaPessoaRepository(sessionDb)
        seedDb = FactCdaPessoaSeeder(repo, cda_pessoa_repo)
        seedDb.seed_fact_cda_pessoa()
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
    print("Database from fact_cda_pessoa seeded successfully.\n")

if __name__ == "__main__":
    run()
