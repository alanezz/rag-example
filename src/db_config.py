import os

db_user = os.getenv("POSTGRES_USER", "user_rag_example")
db_password = os.getenv("POSTGRES_PASSWORD", "password_rag_example")
db_database = os.getenv("POSTGRES_DB", "db_rag_example")
db_host = os.getenv("POSTGRES_HOST", "db")
db_port = os.getenv("POSTGRES_PORT", "5432")
