from files.files import FileHandler
from formater.staff_info import StaffInfoFormatter
from apis.api import register_staff
def print_menu() -> int:
    print("1. Register Staff")
    print("2. View Staff Details")
    print("3. Exit")
    return int(input())

def register_new_staff():
    file_handler = FileHandler()
    staff_details = file_handler.get_staff_details()
    # formatter = StaffInfoFormatter(staff_details)
    # formatter.print_staff_infos()
    print(f"Available Staff to Register: "
          f"{', '.join(staff.get('full_name') for staff in staff_details)}")
    option = int(input())
    if option > len(staff_details):
        return 
    if option < 1:
        return
    selected_staff = staff_details[option - 1]
    register_staff(selected_staff)
    main()

def get_all_staffs(api):
    staffs = api.get_all_staffs()
    for staff in staffs:
        print(f"ID: {staff.get('staff_id')}, Name: {staff.get('full_name')}")
def main():
    choice = print_menu()
    if choice == 1:
        register_new_staff()
    # elif choice == 2:
    #     view_staff_details()
    # elif choice == 3:
    #     exit()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()