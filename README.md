# PERSONAL-EXPENSE-TRACKER-
The Personal Expense Tracker is a menu-driven application developed using Python to help users manage and track their daily expenses efficiently. It provides a simple command-line interface through which users can record, view, search, and delete their expense details.

## Project Overview

The **Personal Expense Tracker** is a simple, menu-driven application developed using Python. It helps users record, manage, and monitor their personal expenses through an interactive command-line interface.

Users can add new expenses, view their expense records, calculate total spending, generate category-wise summaries, search for expenses using unique IDs, and delete existing records.

This project demonstrates the use of basic Python programming concepts and data structures in developing a practical real-world application.

## Features

The application provides the following functionalities:

1. **Add Expense:** Add a new expense by entering its unique ID, category, description, and amount.
2. **View All Expenses:** Display all recorded expenses with their respective details.
3. **Total Expenses:** Calculate and display the total amount spent.
4. **Category-Wise Summary:** Display the total expenditure for each category.
5. **Search Expense:** Search for a particular expense using its unique expense ID.
6. **Delete Expense:** Remove an existing expense record using its ID.
7. **Exit:** Safely exit the application.

## Available Expense Categories

The application supports the following categories:

- Food
- Transport
- Entertainment
- Miscellaneous
- Education
- Shopping

## Technologies Used

- **Programming Language:** Python
- **Interface:** Command-Line Interface (CLI)
- **Data Storage:** Python Dictionaries
- **Data Structures:** Dictionary, List, and Tuple

## Python Concepts Used

This project implements several fundamental Python concepts:

- **Dictionaries:** Store expense records using unique expense IDs as keys.
- **Lists:** Maintain the available expense categories.
- **Tuples:** Store individual expense details, including category, description, and amount.
- **Functions:** Divide the program into smaller, reusable modules.
- **Loops:** Use a while loop to keep the application running until the user exits.
- **Conditional Statements:** Handle user choices and validate inputs.
- **Exception Handling:** Handle invalid numerical inputs using try-except blocks.
- **Dictionary Operations:** Add, access, search, update summaries, and delete expense records.

## How to Run the Project

### Prerequisites

- Python 3.x installed on your computer.
- Any Python-supported code editor, such as VS Code, PyCharm, or IDLE.

### Installation and Execution

**Step 1:** Download or clone this project to your computer.

**Step 2:** Open the project folder in your code editor.

**Step 3:** Save the Python code in a file named:

`expense_tracker.py`

**Step 4:** Open the terminal and execute the following command:

```bash
python expense_tracker.py
```

**Step 5:** The main menu will appear, allowing you to select the desired operation.

## Sample Output

```text
-------PERSONAL EXPENSE TRACKER--------

1. Add Expense
2. View All Expenses
3. Total Expenses
4. Category Wise Summary
5. Search Expense by ID
6. Delete Expense by ID
7. Exit

Enter your choice: 1

-------ADD AN EXPENSE-------

Enter the expense ID: E101
Available Categories: Food, Transport, Entertainment,
Miscellaneous, Education, Shopping

Enter the category of the expense: Food
Enter the description of the expenses: Lunch
Enter the amount of the expense: 150

EXPENSE ADDED SUCCESSFULLY!
```

## Data Storage Structure

The application uses a Python dictionary named `expenses` to store all expense records.

Each expense is stored using a unique expense ID as its key, while the corresponding value is a tuple containing three elements:

```python
expenses = {
    "E101": ("Food", "Lunch", 150.0),
    "E102": ("Transport", "Bus Ticket", 50.0)
}
```

This structure makes it easy to access, search, and delete individual expense records.

## Limitations

- Expense records are stored temporarily in memory.
- All records are lost when the program is closed.
- The application does not use a database or external file for permanent storage.
- It operates through a command-line interface rather than a graphical user interface.

## Future Scope

The project can be enhanced by introducing additional functionalities such as:

- Permanent data storage using files or databases.
- Monthly and weekly expense reports.
- Budget setting and tracking.
- Graphical representation of expenses using charts.
- A graphical user interface (GUI).

## Conclusion

The Personal Expense Tracker demonstrates how fundamental Python concepts and data structures can be combined to create a useful expense management application. It provides basic expense tracking functionalities while helping develop practical programming and problem-solving skills.

AUTHOR
PRIYANSHU 
