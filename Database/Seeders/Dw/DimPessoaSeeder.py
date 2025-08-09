from Database.dw import SessionLocal
from Database.db import SessionLocal as SessionDb
from App.Repositories.Dw.DimPessoa.DimPessoaRepository import DimPessoaRepository
from App.Repositories.Db.Pessoa.PessoaRepository import PessoaRepository


class DimPessoaSeeder:
    def __init__(self, dim_pessoa_repo, pessoa_repo):
        self.dim_pessoa_repo = dim_pessoa_repo
        self.pessoa_repo = pessoa_repo

    def seed_dim_pessoa(self) -> None:
        dim_pessoalist = self.pessoa_repo.get_all()
        self.dim_pessoa_repo.save_all(dim_pessoalist)

def run():
    print("Seeding dim_pessoa...\n")
    session = SessionLocal()
    sessionDb = SessionDb()
    try:
        repo = DimPessoaRepository(session)  
        pessoa_repo = PessoaRepository(sessionDb)
        seedDb = DimPessoaSeeder(repo, pessoa_repo)
        seedDb.seed_dim_pessoa()
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
    print("Database from dim_pessoa seeded successfully.\n")

if __name__ == "__main__":
    run()
