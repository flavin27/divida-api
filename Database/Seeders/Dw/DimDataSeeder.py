from Database.dw import SessionLocal
from Database.db import SessionLocal as SessionDb
from App.Repositories.Db.Cda.CdaRepository import CdaRepository
from App.Repositories.Dw.DimData.DimDataRepository import DimDataRepository
from Database.Parsers.Dw.dataParser import DimDataParser


class DimDataSeeder:
    def __init__(self, dim_data_repo, cda_repo):
        self.dim_data_repo = dim_data_repo
        self.cda_repo = cda_repo

    def seed_dim_data(self) -> None:
        cda_list = self.cda_repo.get_all()

        dim_data_parser = DimDataParser()

        dim_data_list = dim_data_parser.parse_cda_data(cda_list)
        self.dim_data_repo.save_all(dim_data_list)

def run():
    print("Seeding dim_data...\n")
    session = SessionLocal()
    sessionDb = SessionDb()
    try:
        repo = DimDataRepository(session)  
        cda_repo = CdaRepository(sessionDb)
        seedDb = DimDataSeeder(repo, cda_repo)
        seedDb.seed_dim_data()
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
    print("Database from dim_data seeded successfully.\n")

if __name__ == "__main__":
    run()
