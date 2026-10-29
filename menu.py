from functions import *
from services import *

def show_menu():
    while True:
        print("-" * 27)
        print("|" + "-" * 3 + "Service Status Tool" + "-" * 3 + "|")
        print("-" * 27)
        print(f"| 1. {'Show all services':<20} |")
        print(f"| 2. {'Show one service':<20} |")
        print(f"| 3. {'Add service':<20} |")
        print(f"| 4. {'Change status':<20} |")
        print(f"| 5. {'Delete service':<20} |")
        print(f"| 6. {'Exit':<20} |")
        print("-" * 27)
        choice = input(f"| {'You choice... ':<15}")
        print("-" * 27)

        if choice == "1":
            show_services(services)

        elif choice == "2":
            show_one_service(services)

        elif choice == "3":
            add_service(services)

        elif choice == "4":
            change_status(services)

        elif choice == "5":
            delete_service(services)

        elif choice == "6":
            print("-" * 27)
            print("| Services Tool Stopped...")
            print("-" * 27)
            break

        else:
            print("| Wrong Choice. Try again.")


