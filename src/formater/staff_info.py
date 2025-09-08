

class StaffInfoFormatter:
    def __init__(self, staff_info: list[dict[str, str | int]]):
        self.staff_info = staff_info 
    def print_staff_infos(self) -> None:
        count = 1
        for staff in self.staff_info:
            print(
                f"Staff {count}: \n"
                f"\tFull Name: {staff.get('full_name')},\n"
                f"\tStaff ID: {staff.get('staff_id')},"
            )
            count += 1