depend_on_everywhere:
	pip3 freeze > requirements.txt

start:
	uvicorn src.main:app --host '0.0.0.0' --port 8181 --reload

installation_dependencies:
	pip3 install -r requirements.txt

docker_build:
	docker build -f deploy/Dockerfile -t powduck/chia_signature:v1 .

