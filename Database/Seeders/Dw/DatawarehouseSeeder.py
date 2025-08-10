from Database.Seeders.Dw.DimDataSeeder import run as run_dim_data
from Database.Seeders.Dw.DimNaturezaDividaSeeder import run as run_dim_natureza_divida
from Database.Seeders.Dw.DimPessoaSeeder import run as run_dim_pessoa
from Database.Seeders.Dw.DimSituacaoCdaSeeder import run as run_dim_situacao_cda

class DatawarehouseSeeder:

    def run(self):
        print("Starting Datawarehouse Seeder...")

        # Run individual seeders
        run_dim_natureza_divida()
        run_dim_pessoa()
        run_dim_situacao_cda()
        run_dim_data()

        print("Datawarehouse Seeder completed successfully.")

if __name__ == "__main__":
    seeder = DatawarehouseSeeder()
    seeder.run()