
# Default target: build and run
all: build run

# Build target: pull the latest nginx image
build:
	@echo "Pulling NGINX Docker image..."
	docker-compose build

# Run target: run the nginx container
run:
	@echo "Running NGINX container..."
	docker-compose up
