from Database.dw import SessionLocal
from Database.db import SessionLocal as SessionDb
from App.Repositories.Db.Recuperacao.RecuperacaoRepository import RecuperacaoRepository
from App.Repositories.Dw.FactRecuperacao.FactRecuperacaoRepository import FactRecuperacaoRepository
from App.Models.Dw.FactCda import FactCda


class FactRecuperacaoSeeder:
    def __init__(self, fact_recuperacao_repo, recuperacao_repo):
        self.fact_recuperacao_repo = fact_recuperacao_repo
        self.recuperacao_repo = recuperacao_repo

    def seed_fact_recuperacao(self) -> None:
        recuperacao_list = self.recuperacao_repo.get_all()
        self.fact_recuperacao_repo.save_all(recuperacao_list)

def run():
    print("Seeding fact recuperacao...\n")
    session = SessionLocal()
    sessionDb = SessionDb()
    try:
        repo = FactRecuperacaoRepository(session)  
        recuperacao_repo = RecuperacaoRepository(sessionDb)
        seedDb = FactRecuperacaoSeeder(repo, recuperacao_repo)
        seedDb.seed_fact_recuperacao()
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
    print("Database from fact_recuperacao seeded successfully.\n")

if __name__ == "__main__":
    run()
