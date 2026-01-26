# Portfolio Automation Makefile

.PHONY: build up down logs restart clean help

help:
	@echo "Available commands:"
	@echo "  make build   - Build the Docker images"
	@echo "  make up      - Start the application in the background"
	@echo "  make down    - Stop and remove containers"
	@echo "  make restart - Restart the application"
	@echo "  make logs    - View real-time logs"
	@echo "  make clean   - Remove all containers, networks, and volumes"

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

restart:
	docker-compose restart

logs:
	docker-compose logs -f

clean:
	docker-compose down -v --rmi all --remove-orphans
