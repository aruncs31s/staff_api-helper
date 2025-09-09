# Staff API Helper


A Python-based helper application for interacting with a Staff Management API. This tool provides a command-line interface and API client for managing staff information, including staff registration, retrieval, and qualification management.

## Features

- **Staff Registration**: Register new staff members with comprehensive details
- **Staff Retrieval**: Get information about all registered staff members  
- **Qualification Management**: Add qualifications to existing staff members
- **Interactive CLI**: User-friendly command-line interface for all operations
- **JSON Data Handling**: Efficient handling of staff data through JSON files

## Installation

### Prerequisites

- Python 3.7+
- `requests` library

### Setup

1. Clone the repository:
```bash
git clone https://github.com/aruncs31s/staff_api-helper.git
cd staff_api-helper
```

2. Install dependencies:
```bash
pip install requests
```

3. Ensure your Staff API server is running on `http://127.0.0.1:9090`

## Usage

### CLI Interface

Run the application:
```bash
cd src
python app.py
```

The CLI provides the following options:
1. **Register Staff** - Register a new staff member from the JSON data file
2. **Get All Staffs** - Display all registered staff members
3. **Create Qualification** - Add a qualification to an existing staff member
4. **Exit** - Close the application

#### CLI Usage Examples

**Example 1: Registering Staff**
```
$ python app.py
1. Register Staff
2. Get All Staffs
3. Create Qualification
4. Exit
1
Available Staff to Register: Arun CS, Praveen ABC
1
Registering staff: Arun CS With ID: G1_EC 
Staff Arun CS Registered Successfully
```

**Example 2: Viewing All Staff**
```
$ python app.py
1. Register Staff
2. Get All Staffs
3. Create Qualification
4. Exit
2
ID: G1_EC, Name: Arun CS
ID: G2_EC, Name: Praveen ABC
```

**Example 3: Adding Qualification**
```
$ python app.py
1. Register Staff
2. Get All Staffs
3. Create Qualification
4. Exit
3
Enter Staff ID: G1_EC
Enter Qualification Details:
Degree (as integer): 1
Discipline: Computer Science
POST: URL http://127.0.0.1:9090/api/v1/staff/G1_EC/qualification
Data: {'degree': 1, 'discipline': 'Computer Science'}
Status Code: 201
```

### Configuration

The application uses a configuration file located at `data/new_staff_details.json` containing sample staff data. You can modify this file to add your own staff information.

## API Documentation

The application interacts with a Staff Management API running on `http://127.0.0.1:9090/api/v1/staff`. Below are the available endpoints and their corresponding curl commands.

### Base URL
```
http://127.0.0.1:9090/api/v1/staff
```

### Endpoints

#### 1. Register Staff Member

**Endpoint**: `POST /api/v1/staff`

**Description**: Register a new staff member in the system.

**Request Headers**:
```
Content-Type: application/json
Accept: application/json
```

**Request Body Schema**:
```json
{
  "dept_id": 2,
  "join_date": "2025-09-08T00:00:00+05:30",
  "staff_id": "G1_EC",
  "full_name": "John Doe",
  "type": 1,
  "contract_type": 2,
  "email": "john.doe@example.com",
  "phone": "1234567890",
  "gender": "Male"
}
```

**Curl Example**:
```bash
curl -X POST http://127.0.0.1:9090/api/v1/staff \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{
    "dept_id": 2,
    "join_date": "2025-09-08T00:00:00+05:30",
    "staff_id": "G1_EC",
    "full_name": "Arun CS",
    "type": 1,
    "contract_type": 2,
    "email": "arun.cs@example.com",
    "phone": "1234567890",
    "gender": "Male"
  }'
```

**Success Response (201 Created)**:
```json
{
  "status": "success",
  "message": "Staff registered successfully",
  "data": {
    "staff_id": "G1_EC",
    "full_name": "Arun CS"
  }
}
```

#### 2. Get All Staff Members

**Endpoint**: `GET /api/v1/staff`

**Description**: Retrieve information about all registered staff members.

**Curl Example**:
```bash
curl -X GET http://127.0.0.1:9090/api/v1/staff \
  -H "Accept: application/json"
```

**Success Response (200 OK)**:
```json
{
  "status": "success",
  "data": [
    {
      "id": 1,
      "user_id": 1000,
      "dept_id": 2,
      "join_date": "2025-09-08T00:00:00+05:30",
      "staff_id": "G1_EC",
      "type": 1,
      "full_name": "Arun CS",
      "gender": "Male",
      "phone": "1234567890",
      "status": 3,
      "create_time": "2025-09-08T12:41:45.485492164+05:30",
      "update_time": "2025-09-08T12:41:45.485492164+05:30",
      "contract_type": 2,
      "faculty_on_deputation": 0
    },
    {
      "id": 2,
      "user_id": 1000,
      "dept_id": 2,
      "join_date": "2025-09-08T00:00:00+05:30",
      "staff_id": "G2_EC",
      "type": 1,
      "full_name": "Praveen ABC",
      "gender": "Male",
      "phone": "1234567890",
      "status": 3,
      "create_time": "2025-09-08T12:58:07.979327456+05:30",
      "update_time": "2025-09-08T12:58:07.979327456+05:30",
      "contract_type": 2,
      "faculty_on_deputation": 0
    }
  ]
}
```

#### 3. Register Staff Qualification

**Endpoint**: `POST /api/v1/staff/{staff_id}/qualification`

**Description**: Add a qualification to an existing staff member.

**Path Parameters**:
- `staff_id` (string): The unique identifier of the staff member

**Request Headers**:
```
Content-Type: application/json
Accept: application/json
```

**Request Body Schema**:
```json
{
  "degree": 1,
  "discipline": "Computer Science"
}
```

**Curl Example**:
```bash
curl -X POST http://127.0.0.1:9090/api/v1/staff/G1_EC/qualification \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{
    "degree": 1,
    "discipline": "Computer Science"
  }'
```

**Success Response (201 Created)**:
```json
{
  "id": 7,
  "staff_id": 1,
  "degree": 1,
  "discipline": "Electronics",
  "university": "",
  "percentage": 0,
  "year": 2000,
  "sort": 0,
  "type": 0,
  "category": 0,
  "status": 0,
  "start_year": 2000,
  "file": "http://someurl.com/image.png",
  "remarks": "Not Set",
  "qualification": 0,
  "cgpa": 0
}
```

## Data Models

### Staff Model
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `dept_id` | integer | Yes | Department ID |
| `join_date` | string (ISO 8601) | Yes | Date of joining |
| `staff_id` | string | Yes | Unique staff identifier |
| `full_name` | string | Yes | Full name of the staff member |
| `type` | integer | Yes | Staff type identifier |
| `contract_type` | integer | Yes | Contract type identifier |
| `email` | string | Yes | Email address |
| `phone` | string | Yes | Phone number |
| `gender` | string | Yes | Gender (Male/Female) |

### Qualification Model
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `degree` | integer | Yes | Degree type identifier |
| `discipline` | string | Yes | Field of study/discipline |

## File Structure

```
staff_api-helper/
├── src/
│   ├── app.py                      # Main application entry point
│   ├── staff_registration.ipynb    # Jupyter notebook for development/testing
│   ├── apis/
│   │   ├── __init__.py
│   │   └── api.py                  # API client class
│   ├── files/
│   │   ├── __init__.py
│   │   └── files.py                # File handling utilities
│   └── formater/
│       ├── __init__.py
│       └── staff_info.py           # Staff information formatter
├── data/
│   └── new_staff_details.json      # Sample staff data
├── test-api-endpoints.sh           # Automated API testing script
├── README.md                       # This documentation file
├── .gitignore                      # Git ignore patterns
└── LICENSE                         # MIT License
```

## Error Handling

The application includes comprehensive error handling for common scenarios:

- **Invalid Staff ID**: When trying to register qualifications for non-existent staff
- **Network Errors**: Connection issues with the API server
- **Invalid JSON**: Malformed request data
- **HTTP Status Errors**: Non-2xx responses from the server

Common error responses:
```bash
# 404 Not Found
curl -X POST http://127.0.0.1:9090/api/v1/staff/INVALID_ID/qualification \
  -H "Content-Type: application/json" \
  -d '{"degree": 1, "discipline": "Computer Science"}'

# 400 Bad Request
curl -X POST http://127.0.0.1:9090/api/v1/staff \
  -H "Content-Type: application/json" \
  -d '{"invalid": "data"}'
```

## Testing the API

You can test all endpoints using the provided curl commands. Make sure your API server is running before executing any requests.

### Automated Test Script

A comprehensive test script `test-api-endpoints.sh` is provided to test all API endpoints:

```bash
# Make the script executable (if not already)
chmod +x test-api-endpoints.sh

# Run the test script
./test-api-endpoints.sh
```

This script will:
1. Test connection to the API server
2. Register sample staff members from the data file
3. Add qualifications to the registered staff
4. Retrieve all staff to verify the operations

### Manual Testing Examples

#### Quick Connection Test
```bash
# Test if the API server is running
curl -X GET http://127.0.0.1:9090/api/v1/staff \
  -H "Accept: application/json"
```

#### Register a Test Staff Member
```bash
curl -X POST http://127.0.0.1:9090/api/v1/staff \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{
    "dept_id": 1,
    "join_date": "2025-01-01T00:00:00+00:00",
    "staff_id": "TEST_001",
    "full_name": "Test User",
    "type": 1,
    "contract_type": 1,
    "email": "test@example.com",
    "phone": "9999999999",
    "gender": "Male"
  }'
```

#### Add Qualification to Test Staff
```bash
curl -X POST http://127.0.0.1:9090/api/v1/staff/TEST_001/qualification \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{
    "degree": 1,
    "discipline": "Software Engineering"
  }'
```

### Response Status Codes

| Code | Meaning | Description |
|------|---------|-------------|
| 200 | OK | Request successful (GET operations) |
| 201 | Created | Resource created successfully (POST operations) |
| 400 | Bad Request | Invalid request data or format |
| 404 | Not Found | Resource not found (invalid staff_id) |
| 500 | Internal Server Error | Server-side error |

## Development

### Jupyter Notebook

For interactive development and testing, a Jupyter notebook is available at `src/staff_registration.ipynb`. This notebook contains:
- Live API testing examples
- Response format exploration
- Development snippets

To use the notebook:
```bash
# Install jupyter if not already installed
pip install jupyter

# Start jupyter notebook
cd src
jupyter notebook staff_registration.ipynb
```

### Python Dependencies

The application requires the following Python packages:
- `requests` - For HTTP API calls
- `json` (built-in) - For JSON data handling

Install dependencies:
```bash
pip install requests
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions about the Staff API Helper, please:
1. Check the error messages for troubleshooting hints
2. Ensure your API server is running on the correct port
3. Verify your JSON data format matches the expected schema
4. Open an issue in the GitHub repository for additional support

See `.github/copilot-instructions.md` for detailed project context and development guidelines.

