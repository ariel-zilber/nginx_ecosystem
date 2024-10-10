# Use the official Python base image
FROM python:3.10-slim

COPY app/* /app/
COPY app/app.py /app/app.py

# Set a working directory in the container
WORKDIR /app
# Copy the requirements file

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Expose the port that Flask will run on (default: 5000)
EXPOSE 5000
RUN ls /app
# Command to run the Flask app
RUN chmod 777 /app/app.py
CMD ["python", "/app/app.py"]
