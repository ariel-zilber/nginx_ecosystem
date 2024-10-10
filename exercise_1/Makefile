# Variables
IMAGE=nginx-exercise-exe:v1
CONTAINER_NAME='nginx-exercise-1'
PORT=8085
 
# Default target: build and run
all: build run

shell:
	@CONTAINER_ID=$$(docker ps | grep ${IMAGE} | awk '{print $$1}') && \
	echo "The value of CONTAINER_ID is: $$CONTAINER_ID" && \
	docker exec -it    "$$CONTAINER_ID" bash

# Build target: pull the latest nginx image
build:
	@echo "Pulling NGINX Docker image..."
	docker build . -t $(IMAGE)

# Run target: run the nginx container
run:
	@echo "Running NGINX container..."
	docker run --name $(CONTAINER_NAME) -p $(PORT):80 \
	-v ./nginx/html:/usr/share/nginx/html \
	-v ./nginx/conf/fastcgi_params:/etc/nginx/fastcgi_params \
	-v ./nginx/conf/uwsgi_params:/etc/nginx/uwsgi_params \
	-v ./nginx/conf/mime.types:/etc/nginx/mime.types \
	-v ./nginx/conf/nginx.conf:/etc/nginx/nginx.conf \
	-v ./nginx/log:/var/log/nginx \
	-v ./nginx/conf/scgi_params:/etc/nginx/scgi_params \
	-v ./nginx/conf/uwsgi_params:/etc/nginx/uwsgi_params \
	-v ./nginx/conf/conf.d:/etc/nginx/conf.d \
	-d $(IMAGE)

# Stop target: stop the running container
stop:
	@echo "Stopping NGINX container..."
	docker stop $(CONTAINER_NAME)

# Clean target: remove the container
clean:
	@echo "Removing NGINX container..."
	docker rm $(CONTAINER_NAME)

# Rebuild target: stop, remove, and run the container again
rebuild: stop clean run

# Log target: show logs from the running container
logs:
	@echo "Showing logs for NGINX container..."
	docker logs $(CONTAINER_NAME)

# Help target: show available commands
help:
	@echo "Makefile for NGINX Docker container management"
	@echo "Available commands:"
	@echo "  make build   - Pull the latest NGINX image"
	@echo "  make run     - Run the NGINX container"
	@echo "  make stop    - Stop the NGINX container"
	@echo "  make clean   - Remove the NGINX container"
	@echo "  make rebuild - Stop, remove, and rerun the container"
	@echo "  make logs    - Show logs from the NGINX container"
