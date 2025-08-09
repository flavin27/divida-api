from sqlalchemy.orm import Session
from Database.Seeders.Db.CdaSeeder import CdaSeeder
from Database.Seeders.Db.NaturezaDividaSeeder import run as run_natureza_divida_seeder
from Database.Seeders.Db.PessoaSeeder import run as run_pessoa_seeder
from Database.Seeders.Db.SituacaoCdaSeeder import run as run_situacao_cda
from Database.Seeders.Db.CdaSeeder import run as run_cda_seeder
from Database.Seeders.Db.historicoCdaSeeder import run as run_historico_cda_seeder
from Database.Seeders.Db.RecuperacaoSeeder import run as run_recuperacao_seeder
from Database.Seeders.Db.CdaPessoaSeeder import run as run_cda_pessoa_seeder


class DatabaseSeeder:
    def __init__(self, session):
        self.session = session
    
    def seed(self):
        print("== Iniciando o seeding do banco de dados ==")
        
        # Ordem importa por causa das FKs
        run_natureza_divida_seeder()
        run_situacao_cda()
        run_pessoa_seeder()
        run_historico_cda_seeder()
        run_cda_seeder()
        run_recuperacao_seeder()
        run_cda_pessoa_seeder()


        print("== Seeding do banco de dados concluído ==")


def run():
    session = Session()
    try:
        seeder = DatabaseSeeder(session)
        seeder.seed()
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Erro durante o seeding: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    run()

