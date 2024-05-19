FROM python:3.8-alpine

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r re.txt

# Copy the application code into the container
COPY . .

# Expose port 5000
EXPOSE 5000

# Start the Flask application
CMD ["flask", "run"]