from app import create_app
from logging.config import fileConfig
from alembic import context
from app.models import db

app = create_app()


# Configuração de logging do Alembic
fileConfig(context.config.config_file_name)

# Definir o modelo para ser usado pelo Alembic
target_metadata = db.metadata

# Configurar o banco de dados a partir do Flask
def run_migrations_online():
    connectable = db.engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if __name__ == '__main__':
    app.run(debug=True)
