FROM python:3.11-slim

# Working directory
WORKDIR /app

# Copying dependencies
COPY requirements.txt /app/

# Installing dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the entire project into the container
COPY testproject /app/

# Open port 8000
EXPOSE 8000

# Command to start Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
