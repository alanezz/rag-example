from langchain_core.documents import Document
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_postgres import PGVector

from db_config import (
    db_user, db_password, db_database,
    db_host, db_port
)

embeddings = HuggingFaceEmbeddings(
    model_name="intfloat/multilingual-e5-base"
)

connection = f"postgresql+psycopg://{db_user}:{db_password}@{db_host}:{db_port}/{db_database}"
collection_name = "constitution"

vectorstore = PGVector(
    embeddings=embeddings,
    collection_name=collection_name,
    connection=connection,
    use_jsonb=True,
)

results = vectorstore.similarity_search("Cómo se cambia la constitución", k=10)

print(results)
