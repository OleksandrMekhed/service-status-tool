def show_services(services):
    print("-" * 27)
    print("|" + "-" * 7 + " Services " + "-" * 8 + "|")
    print("-" * 27)

    for service in services:
        print(f"|{service['name']:<15} : {service['status']}|")
    print("-" * 27)


def show_one_service(services):
    name = input(f"| {'Enter service name: ':<10}")

    for service in services:
        if service['name'] == name:
            print("-" * 27)
            print(f"|{service['name']:<15} : {service['status']}|")
            print("-" * 27)
            return service

    print(f"| Service '{name}' dont found")


def add_service(services):
    name = input("| Enter new name in the service: ").strip()

    new_ser = {
        "name": name,
        "status": "unknown"
    }

    services.append(new_ser)
    print(f"| Service '{name}' add to services")


def change_status(services):
    name = input("| Enter service name: ").strip()

    for service in services:
        if service["name"] == name:
            new_sta = input("| Enter new status (running/stopped/unknown): ").strip()
            service["status"] = new_sta

            print("-" * 27)
            print(f"| Status for '{name}' update for '{new_sta}' |")
            return service

    print(f"| Service '{name}' did not found |")


def delete_service(services):
    del_service = input("| Enter service name for delete service: ")

    for service in services:
        if service["name"] == del_service:
            services.remove(service)

            print("-" * 27)
            print(f"| Service '{service['name']}' - deleted |")
            print("-" * 27)
            return service

    print(f"Service '{del_service}' did not found")

