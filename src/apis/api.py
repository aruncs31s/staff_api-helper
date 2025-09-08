import requests
URL="http://127.0.0.1:9090/api/v1/staff"

class API:
    pass

def register_staff(staff_data: dict[str, str | int]) -> None:
    print(f"Registering staff: {staff_data.get('full_name')} With ID: {staff_data.get('staff_id')} ")
    method = "POST" 
    response = requests.request(method, URL, json=staff_data)
    if response.status_code == 201:
        print(f"Staff {staff_data.get('full_name')} Registered Successfully")
    else:
        print(f"Failed to create staff {staff_data.get('full_name')}. Status Code: {response.status_code}, Response: {response.text}")