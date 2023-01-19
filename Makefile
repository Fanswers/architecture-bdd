.PHONY: help

.DEFAULT_GOAL := build

### DOCKER TASKS ###

compose: # Build image + containers + run
	docker-compose up -d

delete: # Delete container and image
	docker stop "architecture-bdd-flask_api-1"
	docker rm "architecture-bdd-flask_api-1"
	docker image rm architecture-bdd-flask_api