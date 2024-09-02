from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_postgres import PGVector
from openai import OpenAI

client = OpenAI()

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

query = "Cuáles son los derechos fundamentales"

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
