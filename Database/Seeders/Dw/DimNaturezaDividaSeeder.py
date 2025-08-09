from Database.dw import SessionLocal
from Database.db import SessionLocal as SessionDb
from App.Repositories.Db.NaturezaDivida.NaturezaDividaRepository import NaturezaDividaRepository
from App.Repositories.Dw.DimNaturezaDivida.DimNaturezaDividaRepository import DimNaturezaDividaRepository


class DimNaturezaDividaSeeder:
    def __init__(self, dim_natureza_divida_repo, natureza_divida_repo):
        self.dim_natureza_divida_repo = dim_natureza_divida_repo
        self.natureza_divida_repo = natureza_divida_repo

    def seed_dim_natureza_divida(self) -> None:
        dim_natureza_divida_list = self.natureza_divida_repo.get_all()
        self.dim_natureza_divida_repo.save_all(dim_natureza_divida_list)

def run():
    print("Seeding dim_natureza divida...\n")
    session = SessionLocal()
    sessionDb = SessionDb()
    try:
        repo = DimNaturezaDividaRepository(session)  
        natureza_divida_repo = NaturezaDividaRepository(sessionDb)
        seedDb = DimNaturezaDividaSeeder(repo, natureza_divida_repo)
        seedDb.seed_dim_natureza_divida()
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
    print("Database from dim_natureza divida seeded successfully.\n")

if __name__ == "__main__":
    run()
