from Database.db import SessionLocal
from App.Repositories.Db.NaturezaDivida.NaturezaDividaRepository import NaturezaDividaRepository
from Database.Parsers.naturezaDividaParser import NaturezaDividaParser

class NaturezaDividaSeeder:
    def __init__(self, natureza_divida_repo):
        self.natureza_divida_repo = natureza_divida_repo

    def seed_natureza_divida(self, file_path: str) -> None:
        parser = NaturezaDividaParser(file_path)
        natureza_divida_list = parser.parse()
        self.natureza_divida_repo.save_all(natureza_divida_list)

def run():
    print("Seeding natureza divida...\n")
    session = SessionLocal()
    try:
        repo = NaturezaDividaRepository(session)  
        seedDb = NaturezaDividaSeeder(repo)
        seedDb.seed_natureza_divida('data/002.csv')
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
    print("Database from natureza divida seeded successfully.\n")

if __name__ == "__main__":
    run()
