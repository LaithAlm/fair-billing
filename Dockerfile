FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the application files
COPY src/ src/
COPY tests/ tests/

# Set the default command to run tests
CMD ["python", "-m", "unittest", "discover", "-s", "tests"]
