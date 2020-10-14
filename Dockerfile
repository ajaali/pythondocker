# Use an official Python runtime as a parent image
FROM python:3.7-slim-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app /app

# Install any needed packages specified in requirements.txt
RUN pip install -r /app/requirements.txt

# Run main app when the container launches
CMD ["python","mycode/main.py"]