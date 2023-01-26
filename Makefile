.PHONY: help

.DEFAULT_GOAL := build

### DOCKER TASKS ###

compose: # Build images, create containers and run containers
	docker-compose up -d

stop: # Stop containers
	docker stop "architecture-bdd-ofelia-scheduler-1"
	docker stop "architecture-bdd-flask-api-1"

rm-containers: # Delete containers
	docker rm "architecture-bdd-flask-api-1"
	docker rm "architecture-bdd-scraper-1"
	docker rm "architecture-bdd-streamlit-interface-1"
	docker rm "architecture-bdd-ofelia-scheduler-1"

rm-images: # Delete images
	docker image rm architecture-bdd-flask_api
	docker image rm architecture-bdd-scraper
	docker image rm architecture-bdd-streamlit-interface
