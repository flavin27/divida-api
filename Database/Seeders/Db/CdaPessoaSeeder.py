from Database.db import SessionLocal
from App.Repositories.Db.CdaPessoa.CdaPessoaRepository import CdaPessoaRepository
from Database.Parsers.cdaPessoaParser import CdaPessoaParser

class CdaPessoaSeeder:
    def __init__(self, cda_pessoa_repo):
        self.cda_pessoa_repo = cda_pessoa_repo

    def seed_cda(self, file_path: str) -> None:
        parser = CdaPessoaParser(file_path)
        cda_pessoa_list = parser.parse()
        self.cda_pessoa_repo.save_all(cda_pessoa_list)

def run():
    print("Seeding cda pessoas...\n")
    session = SessionLocal()
    try:
        repo = CdaPessoaRepository(session)  
        seedDb = CdaPessoaSeeder(repo)
        seedDb.seed_cda('data/005.csv')
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
    print("Database from cda pessoas seeded successfully.\n")

if __name__ == "__main__":
    run()
