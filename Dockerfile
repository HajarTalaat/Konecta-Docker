# Use an official lightweight Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable for Flask message
ENV APP_MESSAGE="Hello from Docker Container!"

# Expose the port Flask runs on
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]



