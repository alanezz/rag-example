from langchain_core.documents import Document
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters.character import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.pdf import PDFPlumberLoader
from langchain_postgres import PGVector

embeddings = HuggingFaceEmbeddings(
    model_name="intfloat/multilingual-e5-base"
)
tokenizer = embeddings.client.tokenizer

splitter = RecursiveCharacterTextSplitter.from_huggingface_tokenizer(tokenizer, keep_separator=True, add_start_index=True, separators=["\n"], chunk_size=128, chunk_overlap=20)
pdf_loader = PDFPlumberLoader('data/constitucion.pdf')
chunks = pdf_loader.load_and_split(splitter)

connection = "postgresql+psycopg://user_pudato:password_pudato@db:5432/db_pudato"
collection_name = "constitution"

documents = [
        Document(
            page_content=chunk.page_content,
            metadata={**chunk.metadata, "id": i},
        ) for i,chunk in enumerate(chunks)
    ]


vectorstore = PGVector(
    embeddings=embeddings,
    collection_name=collection_name,
    connection=connection,
    use_jsonb=True,
)

vectorstore.add_documents(
    documents, ids=[doc.metadata["id"] for doc in documents]
)
