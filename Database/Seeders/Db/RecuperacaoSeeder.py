from Database.db import SessionLocal
from App.Repositories.Db.Recuperacao.RecuperacaoRepository import RecuperacaoRepository
from Database.Parsers.recuperacaoParser import RecuperacaoParser
from App.Models.Db.Cda import Cda

class RecuperacaoSeeder:
    def __init__(self, recuperacao_repo):
        self.recuperacao_repo = recuperacao_repo

    def seed_recuperacao(self, file_path: str) -> None:
        parser = RecuperacaoParser(file_path)
        recuperacao_list = parser.parse()
        self.recuperacao_repo.save_all(recuperacao_list)

def run():
    print("Seeding recuperacao...\n")
    session = SessionLocal()
    try:
        repo = RecuperacaoRepository(session)  
        seedDb = RecuperacaoSeeder(repo)
        seedDb.seed_recuperacao('data/004.csv')
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
    print("Database from recuperacao seeded successfully.\n")

if __name__ == "__main__":
    run()
