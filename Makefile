.PHONY: help

.DEFAULT_GOAL := build

### DOCKER TASKS ###

compose: # Build image + containers + run
	docker-compose up -d

delete: # Delete container and image
	docker stop "architecture-bdd-ofelia-scheduler"
	docker stop "architecture-bdd-flask-api-1"
	docker rm "architecture-bdd-flask-api-1"
	docker rm "architecture-bdd-scraper-1"
	docker rm "architecture-bdd-ofelia-scheduler-1"
	docker image rm architecture-bdd-flask_api
	docker image rm architecture-bdd-scraper
