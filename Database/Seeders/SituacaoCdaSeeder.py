from Database.db import SessionLocal
from App.Repositories.Db.SituacaoCda.SituacaoCdaRepository import SituacaoCdaRepository
from Database.Parsers.situacaoCdaParser import SituacaoCdaParser

class SituacaoCdaSeeder:
    def __init__(self, situacao_cda_repo):
        self.situacao_cda_repo = situacao_cda_repo

    def seed_situacao_cda(self, file_path: str) -> None:
        parser = SituacaoCdaParser(file_path)
        situacao_cda_list = parser.parse()
        self.situacao_cda_repo.save_all(situacao_cda_list)

def run():
    print("Seeding the database from situacao cda...\n")
    session = SessionLocal()
    try:
        repo = SituacaoCdaRepository(session)  
        seedDb = SituacaoCdaSeeder(repo)
        seedDb.seed_situacao_cda('data/003.csv')
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
    print("Database from situacao cda seeded successfully.\n")

if __name__ == "__main__":
    run()
