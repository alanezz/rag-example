build:
	docker compose build

up:
	docker compose up

load-documents:
	docker compose run --rm app poetry run python src/load_documents.py

rag:
	docker compose run --rm app poetry run python src/rag_example.py
