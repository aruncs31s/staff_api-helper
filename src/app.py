from files.files import FileHandler
from formater.staff_info import StaffInfoFormatter
from apis.api import STAFF_API
def print_menu() -> int:
    print("1. Register Staff")
    print("2. Get All Staffs")
    # print("3. View Staff Details")
    print("3. Create Qualification")
    print("4. Exit")
    return int(input())

def register_new_staff(api: STAFF_API):
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
    api.register_staff(selected_staff)
    main()
def get_all_staffs(api: STAFF_API):
    staffs = api.get_all_staffs()
    for staff in staffs:
        print(f"ID: {staff.get('staff_id')}, Name: {staff.get('full_name')}")

def create_new_qualification(api: STAFF_API):
    staff_id = input("Enter Staff ID: ")
    print("Enter Qualification Details:")
    degree  = int(input("Degree (as integer): "))
    discipline = input("Discipline: ")
    data = {
        "degree": degree,
        "discipline": discipline
    }
    resp  = api.register_qualification(staff_id, data = data)
    print(f"Qualification Response: {resp}")




def main():
    
    choice = print_menu()
    if choice == 1:
        api = STAFF_API("http://127.0.0.1:9090/api/v1/staff")
        register_new_staff(api)
    elif choice == 2:
        api = STAFF_API("http://127.0.0.1:9090/api/v1/staff")
        get_all_staffs(api)
    elif choice == 3:
        api = STAFF_API("http://127.0.0.1:9090/api/v1/staff")
        create_new_qualification(api)
    elif choice == 4:
        exit()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()