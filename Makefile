all:
	docker-compose up

build:
	docker-compose up

start:
	docker-compose up --build -d
	docker-compose logs