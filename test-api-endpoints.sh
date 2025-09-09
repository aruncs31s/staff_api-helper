#!/bin/bash

# Staff API Helper - Test Script
# This script tests all the API endpoints documented in README.md
# Make sure your API server is running on http://127.0.0.1:9090 before running this script

BASE_URL="http://127.0.0.1:9090/api/v1/staff"
echo "Testing Staff API Helper endpoints..."
echo "Base URL: $BASE_URL"
echo "================================================"

# Test 1: Get all staff members
echo "1. Testing GET /api/v1/staff (Get all staff members)"
echo "curl -X GET $BASE_URL"
curl -X GET $BASE_URL -H "Accept: application/json" -w "\nHTTP Status: %{http_code}\n\n" || echo "Failed to connect to API server"

# Test 2: Register a new staff member
echo "2. Testing POST /api/v1/staff (Register staff member)"
echo "Registering sample staff member..."
curl -X POST $BASE_URL \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -w "\nHTTP Status: %{http_code}\n\n" \
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
  }' || echo "Failed to connect to API server"

# Test 3: Register another staff member
echo "3. Testing POST /api/v1/staff (Register another staff member)"
echo "Registering second sample staff member..."
curl -X POST $BASE_URL \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -w "\nHTTP Status: %{http_code}\n\n" \
  -d '{
    "dept_id": 2,
    "join_date": "2025-09-08T00:00:00+05:30",
    "staff_id": "G2_EC",
    "full_name": "Praveen ABC",
    "type": 1,
    "contract_type": 2,
    "email": "praveen.abc@example.com",
    "phone": "1234567890",
    "gender": "Male"
  }' || echo "Failed to connect to API server"

# Test 4: Add qualification to first staff member
echo "4. Testing POST /api/v1/staff/{staff_id}/qualification (Add qualification)"
echo "Adding qualification to staff G1_EC..."
curl -X POST "$BASE_URL/G1_EC/qualification" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -w "\nHTTP Status: %{http_code}\n\n" \
  -d '{
    "degree": 1,
    "discipline": "Computer Science"
  }' || echo "Failed to connect to API server"

# Test 5: Add qualification to second staff member
echo "5. Testing POST /api/v1/staff/{staff_id}/qualification (Add another qualification)"
echo "Adding qualification to staff G2_EC..."
curl -X POST "$BASE_URL/G2_EC/qualification" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -w "\nHTTP Status: %{http_code}\n\n" \
  -d '{
    "degree": 2,
    "discipline": "Electronics Engineering"
  }' || echo "Failed to connect to API server"

# Test 6: Get all staff members again to see the changes
echo "6. Testing GET /api/v1/staff again (Verify registrations)"
echo "curl -X GET $BASE_URL"
curl -X GET $BASE_URL -H "Accept: application/json" -w "\nHTTP Status: %{http_code}\n\n" || echo "Failed to connect to API server"

echo "================================================"
echo "API endpoint testing completed!"
echo ""
echo "NOTE: If you see 'Failed to connect to API server' messages,"
echo "make sure your Staff API server is running on http://127.0.0.1:9090"
echo ""
echo "To run the Python CLI application:"
echo "cd src && python app.py"