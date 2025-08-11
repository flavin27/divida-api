from Database.Migrations.db_migrate import migrate
from Database.Migrations.dw_migrate import migrate_dw

def migrate_all():
    migrate()
    migrate_dw()

if __name__ == "__main__":
    migrate_all()