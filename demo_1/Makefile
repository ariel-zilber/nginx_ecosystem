# Variables
IMAGE=nginx-simple-demo-1:v1
CONTAINER_NAME='demo-1'
PORT=8080
 
# Default target: build and run
all: build run

# Build target: pull the latest nginx image
build:
	@echo "Pulling NGINX Docker image..."
	docker build . -t $(IMAGE)

# Run target: run the nginx container
run:
	@echo "Running NGINX container..."
	docker run --name $(CONTAINER_NAME) -p $(PORT):80 -d $(IMAGE)

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
