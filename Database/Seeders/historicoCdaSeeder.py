from Database.db import SessionLocal
from App.Repositories.Db.HistoricoCda.HistoricoCdaRepository import HistoricoCdaRepository  
from Database.Parsers.historicoCdaParser import HistoricoCdaParser

class HistoricoCdaSeeder:
    def __init__(self, historico_cda_repo):
        self.historico_cda_repo = historico_cda_repo

    def seed_cda(self, file_path: str) -> None:
        parser = HistoricoCdaParser(file_path)
        historico_cda_list = parser.parse()
        self.historico_cda_repo.save_all(historico_cda_list)

def run():
    print("Seeding historico cda...\n")
    session = SessionLocal()
    try:
        repo = HistoricoCdaRepository(session)  
        seedDb = HistoricoCdaSeeder(repo)
        seedDb.seed_cda('data/001.csv')
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
    print("Database from historico cda seeded successfully.\n")

if __name__ == "__main__":
    run()
