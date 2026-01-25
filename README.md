# Ticketing System API

A modern IT ticketing system built with FastAPI to streamline ticket management and IT support workflows.

## Overview

This project is a RESTful API for managing IT support tickets. Built with FastAPI, it provides a high-performance, easy-to-use backend for ticket creation, tracking, and management. The system is designed to help IT teams efficiently handle support requests, bug reports, and service requests.

## Key Features

- **Ticket Creation**: Create new support tickets with detailed information
- **Ticket Management**: Track ticket status and progress
- **Fast and Efficient**: Built on FastAPI for high performance and async support
- **Type Safety**: Utilizes Pydantic models for data validation
- **RESTful API**: Clean, intuitive API design following REST principles
- **Automatic Documentation**: Interactive API documentation with Swagger UI and ReDoc

## Technologies Used

- **FastAPI**: Modern, fast web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **Python 3.11+**: Leveraging modern Python features
- **uv**: A fast Python package installer and dependency resolver
- **Uvicorn**: An ASGI server, used to run the FastAPI application

## Installation

### Prerequisites

- Python 3.11 or higher
- uv (a fast Python package installer and dependency resolver)

If you don't have `uv` installed, you can install it using `pipx` (recommended) or `pip`:

```bash
pip install uv
# or
pipx install uv
```

### Setup

```bash
uv pip install -r requirements.txt
# or
uv sync
```

## Usage

### Starting the Server

First, make sure you have installed the project dependencies, including `uvicorn`, using `uv sync` or `uv pip install -r requirements.txt`.

Then, run the application using uvicorn:

```bash
uvicorn src.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

### Interactive API Documentation

Once the server is running, access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Roadmap

Future enhancements planned for this project:

- [ ] Add authentication and authorization
- [ ] Implement ticket retrieval (GET endpoints)
- [ ] Add ticket update and deletion functionality
- [ ] Implement ticket assignment to support staff
- [ ] Add priority levels for tickets
- [ ] Implement ticket filtering and searching
- [ ] Add ticket commenting system
- [ ] Email notifications for ticket updates
- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] User management system
- [ ] Analytics and reporting features

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For questions or support, please open an issue on the GitHub repository.
