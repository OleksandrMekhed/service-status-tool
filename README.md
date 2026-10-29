# Service Status Tool 

A lightweight, modular command-line utility written in Python for monitoring, viewing, and managing local or containerized development services (like Nginx, PostgreSQL, Docker, Redis, etc.).

## Features

* **Interactive Console Menu:** Simple, text-based visual interface with custom formatting.
* **Service Management:**
  * View all services and their current statuses (`running`, `stopped`, `unknown`).
  * Search for a specific service by name.
  * Add new services dynamically to the session.
  * Update service statuses on the fly.
  * Remove services from the list.
* **Modular Architecture:** Clean separation of concerns into entry points, menus, business logic, and data storage.

---

## Project Structure

```text
service_status_tool/
│
├── main.py        # Application entry point (runs the program)
├── menu.py        # Interactive UI loop and user choice handling
├── functions.py   # Core business logic (CRUD operations for services)
└── services.py    # Initial mock data and service registry
```

---

## Requirements

* Python 3.8+ (no external third-party libraries required; uses only the standard library).

---

## Installation & Running

1. Clone the repository (or download the source files into a single directory):

   ```bash
   git clone https://github.com/OleksandrMekhed/service-status-tool.git
   cd service-status-tool
   ```

2. Run the application:

   ```bash
   python main.py
   ```

---

## Usage Example

Once you run `python main.py`, you will see the interactive menu:

```text
---------------------------
|---Service Status Tool---|
---------------------------
| 1. Show all services    |
| 2. Show one service     |
| 3. Add service          |
| 4. Change status        |
| 5. Delete service       |
| 6. Exit                 |
---------------------------
| You choice...
```

Simply type the number corresponding to the action you want to perform and follow the on-screen prompts.

---

## Tech Stack

* **Language:** Python 3
* **UI Library:** Rich
* **Design Patterns:** Modular programming, Separation of Concerns

---