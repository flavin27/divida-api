from Database.db import SessionLocal
from App.Repositories.Db.Pessoa.PessoaRepository import PessoaRepository
from Database.Parsers.pessoaParser import PessoaParser

class PessoaSeeder:
    def __init__(self, pessoa_repo):
        self.pessoa_repo = pessoa_repo

    def seed_pessoa(self, file_path: str) -> None:
        parser = PessoaParser(file_path)
        pessoa_list = parser.parse()
        self.pessoa_repo.save_all(pessoa_list)

def run():
    print("Seeding pessoas...\n")
    session = SessionLocal()
    try:
        repo = PessoaRepository(session)  
        seedDb = PessoaSeeder(repo)
        seedDb.seed_pessoa('data/006.csv')
        seedDb.seed_pessoa('data/007.csv')
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
    print("Database from pessoa seeded successfully.\n")

if __name__ == "__main__":
    run()
