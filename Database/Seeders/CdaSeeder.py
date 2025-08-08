from Database.db import SessionLocal
from App.Repositories.Db.Cda.CdaRepository import CdaRepository
from Database.Parsers.cdaParser import CdaParser

class CdaSeeder:
    def __init__(self, cda_repo):
        self.cda_repo = cda_repo

    def seed_cda(self, file_path: str) -> None:
        parser = CdaParser(file_path)
        cda_list = parser.parse()
        self.cda_repo.save_all(cda_list)

def run():
    print("Seeding cda...\n")
    session = SessionLocal()
    try:
        repo = CdaRepository(session)  
        seedDb = CdaSeeder(repo)
        seedDb.seed_cda('data/001.csv')
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
    print("Database from cda seeded successfully.\n")

if __name__ == "__main__":
    run()
