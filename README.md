# OLS Product Service

OLS Product Service is a RESTful API for managing products in an online store. The service is built using Flask, SQLAlchemy, Redis, and Docker.

## Features

- CRUD operations for products
- Health checks for the service
- Caching for better performance
- Dockerized for easy deployment
- Unit testing and CI/CD

## Installation

### Requirements

- Python 3.8 or later
- MySQL
- Redis

### Clone the repository

```bash
git clone https://github.com/yourusername/ols_product.git
cd ols_product
```

### Create a virtual environment and install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Set up environment variables

Copy `.env-example` to `.env` and update the values according to your database and cache configuration.

```bash
cp .env-example .env
```

### Run the application

```bash
flask run
```

## API Documentation

The API supports the following endpoints:

| Method | Endpoint            | Description                          |
|--------|---------------------|--------------------------------------|
| GET    | /products           | Retrieve a list of all products      |
| POST   | /products           | Create a new product                 |
| GET    | /product/:id        | Retrieve a product by its ID         |
| PUT    | /product/:id        | Update a product by its ID           |
| DELETE | /product/:id        | Delete a product by its ID           |

## Deployment

### Docker

Build the Docker image:

```bash
docker build -t yourusername/ols_product .
```

Run the Docker container:

```bash
docker run -p 5000:5000 --env-file .env yourusername/ols_product
```

### GitHub Actions CI/CD

The repository includes a GitHub Actions workflow that pushes Docker images to Docker Hub upon pushes to the `main`, `dev`, and version tag branches.

To set up this workflow, add the following secrets to your GitHub repository:

- `DOCKER_USERNAME`: Your Docker Hub username
- `DOCKER_PASSWORD`: Your Docker Hub password or access token

## Contributing

Please feel free to submit issues and pull requests for new features or improvements.

## License

This project is licensed under the Apache License.