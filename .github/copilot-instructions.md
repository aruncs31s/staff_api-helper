# GitHub Copilot Instructions for Staff API Helper

This is a Python-based helper application for managing staff data that interacts with the [etlab_backend_go_staff_module](https://github.com/aruncs31s/etlab_backend_go_staff_module) Go backend API.

## Project Overview

This helper tool provides a Python interface for staff management operations including:
- Registering new staff members
- Retrieving all staff information
- Creating and managing staff qualifications

## Technology Stack

- **Language**: Python 3.x
- **HTTP Client**: `requests` library for API communication
- **Data Format**: JSON for data exchange and storage
- **Backend API**: Go-based staff management API using Gin and GORM
- **Architecture**: Client-server architecture with RESTful API communication

## Project Structure

```
staff_api-helper/
├── src/
│   ├── app.py                    # Main application with menu-driven interface
│   ├── apis/
│   │   ├── __init__.py
│   │   └── api.py               # STAFF_API class for HTTP API calls
│   ├── files/
│   │   ├── __init__.py
│   │   └── files.py             # FileHandler class for JSON data operations
│   ├── formater/
│   │   ├── __init__.py
│   │   └── staff_info.py        # StaffInfoFormatter for data presentation
│   └── staff_registration.ipynb  # Jupyter notebook for interactive operations
├── data/
│   └── new_staff_details.json   # Sample staff data for registration
├── README.md
└── LICENSE
```

## Key Components

### 1. Main Application (`src/app.py`)
- Menu-driven console interface
- Handles user interactions and orchestrates API calls
- Functions: `register_new_staff()`, `get_all_staffs()`, `create_new_qualification()`
- Default API base URL: `http://127.0.0.1:9090/api/v1/staff`

### 2. API Client (`src/apis/api.py`)
- **Class**: `STAFF_API`
- **Base URL**: Configurable backend API endpoint
- **Key Methods**:
  - `register_staff(staff_data: dict)`: POST request to register new staff
  - `get_all_staffs()`: GET request to retrieve all staff members
  - `register_qualification(staff_id: str, data: dict)`: POST request to add qualifications

### 3. File Handler (`src/files/files.py`)
- **Class**: `FileHandler`
- Manages JSON data file operations
- **Key Methods**:
  - `read_data()`: Load JSON data from file
  - `write_data(data)`: Save data to JSON file
  - `get_staff_details()`: Extract staff admission details

### 4. Data Formatter (`src/formater/staff_info.py`)
- **Class**: `StaffInfoFormatter`
- Formats and displays staff information
- **Key Methods**:
  - `print_staff_infos()`: Pretty-print staff details

## Data Models

### Staff Data Structure
```json
{
  "dept_id": 2,
  "join_date": "2025-09-08T00:00:00+05:30",
  "staff_id": "G1_EC",
  "full_name": "Arun CS",
  "type": 1,
  "contract_type": 2,
  "email": "arun.cs@example.com",
  "phone": "1234567890",
  "gender": "Male"
}
```

### Qualification Data Structure
```json
{
  "degree": 1,
  "discipline": "Computer Science"
}
```

## API Endpoints

### Staff Management
- `POST /api/v1/staff` - Register new staff member
- `GET /api/v1/staff` - Get all staff members
- `POST /api/v1/staff/{staff_id}/qualification` - Add qualification for staff

### Expected Response Formats
- **Success**: Status 201 (Created) or 200 (OK)
- **Response Body**: JSON with `data` field containing results
- **Error Handling**: Status codes with error messages in response text

## Development Guidelines

### Code Style
- Use type hints for function parameters and return types
- Follow Python naming conventions (snake_case for functions/variables)
- Include docstrings for class methods
- Handle HTTP errors gracefully with appropriate user feedback

### Error Handling Patterns
```python
if response.status_code == 201:
    print(f"Operation successful")
    return response.json()
else:
    print(f"Failed operation. Status Code: {response.status_code}, Response: {response.text}")
    return None
```

### Common Patterns
- Menu-driven user interaction with numbered options
- JSON data validation and extraction using `.get()` method
- HTTP requests with proper headers: `{"Content-Type": "application/json", "Accept": "application/json"}`

## Testing and Development

### Running the Application
```bash
cd src
python app.py
```

### Menu Options
1. Register Staff - Select from predefined staff data
2. Get All Staffs - Display all registered staff
3. Create Qualification - Add qualifications for existing staff
4. Exit - Terminate application

## Integration Notes

- This tool is designed to work with a Go backend using Gin framework and GORM ORM
- API endpoints follow RESTful conventions
- JSON data exchange format for all API communications
- Assumes backend server running on `localhost:9090`

## Future Enhancements

When extending this project, consider:
- Adding configuration file for API base URL
- Implementing authentication/authorization
- Adding data validation for staff information
- Creating unit tests for API client methods
- Adding logging for API requests and responses
- Implementing async operations for better performance

## Dependencies

- `requests`: HTTP library for API communication
- Standard library modules: `json` for data handling

Add new dependencies to a `requirements.txt` file when needed.