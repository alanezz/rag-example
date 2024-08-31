from langchain_core.documents import Document
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_postgres import PGVector

embeddings = HuggingFaceEmbeddings(
    model_name="intfloat/multilingual-e5-base"
)

connection = "postgresql+psycopg://user_pudato:password_pudato@db:5432/db_pudato"  # Uses psycopg3!
collection_name = "constitution"

vectorstore = PGVector(
    embeddings=embeddings,
    collection_name=collection_name,
    connection=connection,
    use_jsonb=True,
)

results = vectorstore.similarity_search("Cómo se cambia la constitución", k=10)

print(results)
