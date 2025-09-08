import requests
URL="http://127.0.0.1:9090/api/v1/staff"

class STAFF_API:
    def __init__(self,base_url: str):
        self.base_url = base_url
    def register_staff(self, staff_data: dict[str, str | int]) -> None:
        print(f"Registering staff: {staff_data.get('full_name')} With ID: {staff_data.get('staff_id')} ")
        method = "POST" 
        response = requests.request(method, self.base_url, json=staff_data)
        if response.status_code == 201:
            print(f"Staff {staff_data.get('full_name')} Registered Successfully")
        else:
            print(f"Failed to create staff {staff_data.get('full_name')}. Status Code: {response.status_code}, Response: {response.text}")
    def get_all_staffs(self) -> list[dict[str, str | int]]:
        """Get all staffs from the Go API Server."""
        method = "GET"
        response = requests.request(method, self.base_url)
        response_data = response.json()
        if response.status_code == 200:
            return response_data.get("data", [])
        else:
            print(f"Failed to fetch staffs. Status Code: {response.status_code}, Response: {response.text}")
            return []
    def register_qualification(self, staff_id: str, data: dict) :
        """Register a new qualification for a staff member."""
        # url = f"{self.base_url}/{staff_id}/qualifications"
        # print(f"URL for qualification registration: {url}")
        # method = "POST"
        # data["staff_id"] = staff_id
        # print(data)
        # response = requests.request(method, url, json=data)
        
        # if response.status_code == 201:
        #     print(f"Qualification registered successfully for Staff ID: {staff_id}")
        #     return response.json()
            
        # else:
        #     print(f"Failed to register qualification for Staff ID: {staff_id}. Status Code: {response.status_code}, Response: {response.text}")
        #     return None
        """Register a new qualification for a staff member"""
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        url = f"{self.base_url}/{staff_id}/qualification"
        print(f"POST: URL {url}")
        print(f"Data: {data}")
        response = requests.post(url, json=data, headers=headers)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 201:
            return response.json()
        else:
            print(f"Error: {response.text}")
            return None