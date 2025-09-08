import json

data_path = 'data/new_staff_details.json'


class FileHandler:
    def __init__(self):
        self.data_path = data_path
    def read_data(self) -> dict:
        with open(self.data_path, 'r') as file:
            return json.load(file)

    def write_data(self, data: list[dict]) -> None:
        with open(self.data_path, 'w') as file:
            json.dump(data, file, indent=4)
    def get_staff_details(self) -> list[dict[str, str | int]]:
        return self.read_data().get("staff_admission_details", [])