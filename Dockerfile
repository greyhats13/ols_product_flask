# Use python:3.8-alpine as the base image for the build stage
FROM python:3.8-alpine as build

# Set environment variables to control Python behavior
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install necessary packages for building
RUN apk add --no-cache build-base

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf ~/.cache/pip

# Set the working directory and copy the app files
WORKDIR /app
COPY . .

# Use python:3.8-alpine as the base image for the release stage
FROM python:3.8-alpine as release

# Set environment variables to control Python behavior
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy the installed Python libraries from the build stage
COPY --from=build /usr/local/lib/python3.8 /usr/local/lib/python3.8
COPY --from=build /usr/local/bin /usr/local/bin

# Set the working directory and copy the app files from the build stage
WORKDIR /app
COPY --from=build /app .

# Expose the port the app runs on
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]