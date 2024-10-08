from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_postgres import PGVector
from openai import OpenAI

from db_config import (
    db_user, db_password, db_database,
    db_host, db_port
)

client = OpenAI()

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

query = "Nacionalidad chilena"

results = vectorstore.similarity_search(query, k=10)
context = ""
for result in results:
    context += result.page_content

system_prompt = f"""
Eres un asistente experto en la constitución chilena.
Una persona te va a hacer una pregunta sobre la constitución y tú debes responderla en base al siguiente contexto:

```
{context}
```

Para responder la pregunta usa el contexto que te acabamos de pasar. Puede que el contexto esté un poco desordenado, pero confiamos en que podrás responder.
"""

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system", "content": system_prompt
        },
        {
            "role": "user",
            "content": query
        }
    ]
)

print("##### Contexto #####")
print(context)
print("##### Respuesta #####")
print(completion.choices[0].message.content)
