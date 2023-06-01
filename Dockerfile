# Use the official Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Update ubuntu
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install zbar-tools -y
RUN apt-get install libzbar-dev -y
RUN apt-get update && apt-get install libgl1  -y

# Install project dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY . .

# Set the command to run when the container starts
CMD ["uvicorn", "main:app", "--reload"]
