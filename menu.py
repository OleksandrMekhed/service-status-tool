from functions import *
from services import services
from rich.console import Console
from rich.panel import Panel

console = Console(force_terminal=True, color_system="truecolor")


def show_menu():
    while True:
        console.print(Panel.fit(
            "[bold cyan]1.[/bold cyan] Show all services\n"
            "[bold cyan]2.[/bold cyan] Show one service\n"
            "[bold cyan]3.[/bold cyan] Add service\n"
            "[bold cyan]4.[/bold cyan] Change status\n"
            "[bold cyan]5.[/bold cyan] Delete service\n"
            "[bold red]6.[/bold red] Exit",
            title="[bold magenta]Service Status Tool [/bold magenta]",
            border_style="cyan"
        ))

        choice = input("Your choice... ").strip()
        console.print()


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
            console.print("[bold red]Services Tool Stopped... Goodbye![/bold red]")
            break

        else:
            console.print("[bold yellow] Wrong Choice. Try again.[/bold yellow]\n")
