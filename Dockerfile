# Use official Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy project files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask uses
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
