import os

DB_PSW = os.environ.get("DB_PSW", "dev_psw")
DB_USER = os.environ.get("DB_USER", "dev_user")
DB_NAME = os.environ.get("DB_NAME", "dev_db")
DB_HOST = os.environ.get("DB_HOST", "db")
postgres_local_base = f"postgresql://{DB_USER}:{DB_PSW}@{DB_HOST}/{DB_NAME}"
