# RAG Example

Para correr este código necesitamos `docker` y `docker compose` instalado. Tiene un `Makefile` con algunos comandos útiles, así que para correrlo en Windows debes ver cómo instalar `make`.

A grandes rasgos, echamos a correr dos servicios:

1. Una base de datos PSQL + PGVector.
2. Un computador con las dependencias de Python necesarias para correr nuestros scripts.

Tenemos 3 scripts:

1. `load_documents.py`: carga los datos en PGVector.
2. `search.py`: un ejemplo de cómo buscar documentos.
3. `rag_example.py`: un ejemplo de cómo pasar contexto a un LLM para obtener respuestas a medida.

Para poder correr `rag_example` necesitamos una API Key de OpenAI.

**Importante**: necesitamos crear en la carpeta raíz un `.env` con los siguientes valores:

```
# Local DB
POSTGRES_USER="user_rag_example"
POSTGRES_PASSWORD="password_rag_example"
POSTGRES_DB="db_rag_example"
POSTGRES_HOST="db"
POSTGRES_PORT="5432"

OPENAI_API_KEY=<Llave de OpenAI>
```

### Ejecución

Para cargar los documentos corremos:

```Bash
make load-documents
```

Esto se demora un tiempo en cargar. Para ejecutar el ejemplo de RAG corremos:

```Bash
make rag
```
