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
- **Python 3.10+**: Leveraging modern Python features

## Project Objectives

The primary objectives of this ticketing system are to:

1. **Simplify Ticket Management**: Provide an intuitive API for creating and managing IT support tickets
2. **Improve Response Times**: Enable quick ticket creation and status tracking
3. **Ensure Data Integrity**: Use strong typing and validation to maintain data quality
4. **Scale Efficiently**: Leverage FastAPI's async capabilities for high-performance operations
5. **Developer-Friendly**: Offer automatic API documentation and easy integration

## Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Carter907/ticketing-system-api.git
cd ticketing-system-api
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install fastapi uvicorn[standard] pydantic
```

## Usage

### Starting the Server

Run the application using uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Interactive API Documentation

Once the server is running, access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Create Ticket

**Endpoint**: `POST /tickets/create`

**Headers**:
- `bingus_type`: Custom header for request type
- `content_type`: Content type of the request

**Request Body**:
```json
{
  "id": 1,
  "subject": "Unable to access email",
  "description": "User cannot log into their email account",
  "status": "not started"
}
```

**Response**:
```json
{
  "id": 1,
  "subject": "Unable to access email",
  "description": "User cannot log into their email account",
  "status": "not started"
}
```

## Data Models

### Ticket

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | integer | Yes | Unique ticket identifier |
| subject | string | Yes | Brief summary of the issue |
| description | string | No | Detailed description of the issue |
| status | string | Yes | Current ticket status (e.g., "not started", "in progress", "completed") |

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

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For questions or support, please open an issue on the GitHub repository.
