from rich.console import Console
from rich.table import Table


console = Console(force_terminal=True, color_system="truecolor")


def show_services(services):
    table = Table(title="Services Status", title_style="bold magenta", border_style="cyan")

    table.add_column("Service Name", style="bold cyan", no_wrap=True)
    table.add_column("Status", style="bold")

    for service in services:
        status = service["status"]
        if status == "running":
            status_styled = "[green]running[/green]"
        elif status == "stopped":
            status_styled = "[red]stopped[/red]"
        else:
            status_styled = f"[yellow]{status}[/yellow]"

        table.add_row(service["name"], status_styled)

    console.print(table)


def show_one_service(services):
    name = input("Enter service name: ").strip()

    for service in services:
        if service['name'] == name:
            status = service['status']
            if status == "running":
                status_styled = "[green]running[/green]"
            elif status == "stopped":
                status_styled = "[red]stopped[/red]"
            else:
                status_styled = f"[yellow]{status}[/yellow]"

            console.print(f"\n[bold cyan]{service['name']}[/bold cyan] : {status_styled}\n")
            return service

    console.print(f"[red]Service '{name}' not found[/red]")


def add_service(services):
    name = input("Enter new service name: ").strip()

    new_ser = {
        "name": name,
        "status": "unknown"
    }

    services.append(new_ser)
    console.print(f"[green]✔ Service '{name}' added successfully![/green]")


def change_status(services):
    name = input("Enter service name: ").strip()

    for service in services:
        if service["name"] == name:
            new_sta = input("Enter new status (running/stopped/unknown): ").strip()
            service["status"] = new_sta

            console.print(f"[green]✔ Status for '{name}' updated to '{new_sta}'![/green]")
            return service

    console.print(f"[red]Service '{name}' not found[/red]")


def delete_service(services):
    del_service = input("Enter service name to delete: ").strip()

    for service in services:
        if service["name"] == del_service:
            services.remove(service)
            console.print(f"[red]✖ Service '{del_service}' deleted.[/red]")
            return service

    console.print(f"[red]Service '{del_service}' not found[/red]")
