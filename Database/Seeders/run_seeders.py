from Database.Seeders.Db.DatabaseSeeder import run as run_db_seeder
from Database.Seeders.Dw.DatawarehouseSeeder import run as run_dw_seeder

def run_seeders():
    run_db_seeder()
    run_dw_seeder()


if __name__ == "__main__":
    run_seeders()