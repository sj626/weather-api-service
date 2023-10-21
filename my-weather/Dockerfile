# Use the official Python image as the base image
FROM python:3.12-slim
# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .
ENV API_KEY="a54f5e809d19b466ea9473efa696d098"
# Install any dependencies
RUN pip install -r requirements.txt

# Copy the Python application code into the container
COPY . .

# Expose the port the application will run on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "weather.py"]

