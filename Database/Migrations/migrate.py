# Database/Migrations/migrate.py

from Database.Migrations.Db.create_cdas_table import run as run_cda
from Database.Migrations.Db.create_naturezaDividas_table import run as run_natureza
from Database.Migrations.Db.create_pessoas_table import run as run_pessoa
from Database.Migrations.Db.create_situacaoCdas_table import run as run_situacao
from Database.Migrations.Db.create_cdas_pessoas_table import run as run_cdas_pessoas
from Database.Migrations.Db.create_recuperacoes_table import run as run_recuperacoes
from Database.Migrations.Db.create_historico_cdas_table import run as run_historico_cdas


def migrate():
    print("== Iniciando execuções das migrations ==")

    # Ordem importa por causa das FKs
    run_natureza()
    run_situacao()
    run_pessoa()
    run_historico_cdas()
    run_cda()
    run_cdas_pessoas()
    run_recuperacoes()

    print("== Todas as migrations foram executadas ==")


if __name__ == "__main__":
    migrate()