# Python CLI Task Manager

A simple and interactive command-line to-do list manager written in Python. Organize your tasks by priorities, mark them as complete, and manage them efficiently from your terminal.

---

### Features

- Add new tasks with custom priority (High, Medium, Low).
- View all tasks, sorted with incomplete tasks and highest priority first, using color-coded visual cues.
- Mark tasks as complete (with strike-through display for done items).
- Change the priority of any task anytime.
- Delete tasks by their unique ID.
- Data is persisted locally in a JSON file (`tasks.json`). No external dependencies required for storage.

---

### Installation

1. Make sure Python 3.x is installed on your system.
2. Download or clone this repository.
3. Place `task_manager.py` in your desired folder. No other files are strictly required — `tasks.json` will be created automatically on first use.

---

### Usage

Run the program from your terminal:

python task_manager.py

You will see a menu:

- 1: View Tasks Sorted by Priority
- 2: Add New Task
- 3: Mark Task as Complete
- 4: Change Task Priority
- 5: Delete Task
- 0: Exit & Save

All tasks will be shown alongside their unique ID, description, & priority level (color-coded).

Example workflow:
- Add a new task and assign a priority (1: High, 2: Medium, 3: Low).
- Mark tasks complete by entering their ID.
- Change priority or delete tasks at any time.

---

### Data Storage

Tasks are stored in a local file called `tasks.json` using standard Python JSON serialization. The app will attempt to recover gracefully from missing or corrupted files.

---

### Code Structure

The main script organizes functionality into the following areas:
- Task loading/saving
- Display & color formatting
- Menu-driven CLI loop
- Task operations (add, complete, prioritize, delete)

---

### Customization

- You can freely modify priorities, change color codes, or customize task fields by editing `task_manager.py`.

---

### License

This project is distributed for educational and personal use. Modify and share freely.

---

### Author

Created by [Your Name].
For feedback or suggestions, open an issue or contact directly.
