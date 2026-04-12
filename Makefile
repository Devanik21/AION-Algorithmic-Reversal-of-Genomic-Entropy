.PHONY: install run test docker-build docker-run lint

install:
	pip install -r requirements.txt

run:
	streamlit run AIoN.py

test:
	python -m pytest tests/

lint:
	flake8 .

docker-build:
	docker build -t aion .

docker-run:
	docker run -p 8501:8501 aion
