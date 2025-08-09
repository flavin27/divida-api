from Database.Migrations.DW.create_dim_datas_table import run as run_dim_datas
from Database.Migrations.DW.create_fact_cdas_table import run as run_fact_cdas
from Database.Migrations.DW.create_fact_cdas_pessoas_table import run as run_fact_cdas_pessoas
from Database.Migrations.DW.create_fact_recuperacoes_table import run as run_fact_recuperacoes
from Database.Migrations.DW.create_dim_naturezaDividas import run as run_dim_natureza_dividas
from Database.Migrations.DW.create_dim_pessoas_table import run as run_dim_pessoas
from Database.Migrations.DW.create_dim_situacaoCdas_table import run as run_dim_situacao_cdas

def migrate_dw():
    print("== Iniciando execuções das migrations do DW ==")

    # Ordem importa por causa das FKs
    run_dim_natureza_dividas()
    run_dim_situacao_cdas()
    run_dim_pessoas()
    run_dim_datas()
    run_fact_cdas()
    run_fact_cdas_pessoas()
    run_fact_recuperacoes()

    print("== Todas as migrations do DW foram executadas ==")

if __name__ == "__main__":
    migrate_dw()