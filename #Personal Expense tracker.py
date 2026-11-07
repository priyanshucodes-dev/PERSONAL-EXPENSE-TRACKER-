#Personal Expense tracker

#Dictionoary to store expenses
expenses = {}

# List of available categories
categories = ["Food" , "Transport" , "Entertainment " , "Miscellaneous" , "Education" , "Shopping" ]

#ADD AN EXPENSES
def add_expense():
    print("\n-------ADD AN EXPENSE------- ")

    expense_id = input("Enter the expense ID: ")

    if expense_id in expenses:
        print("EXPENSE ID ALREADY EXISTS ")
        return

    print("Available Categories:", categories)

    category = input("Enter the category of the expense: ").capitalize()

    if category not in categories:
        print("Invalid category. Please choose from the available categories. ")
        return

    description = input("Enter the description of the expenses: ")

    try:
        amount = float(input("Enter the amount of the expense: "))

        if amount <= 0:
            print("Amount must be a positive number. ")
            return
        
    except ValueError:
        print("Invalid amount. Please enter a valid amount: ")
        return

    #Tuple to store expense details
    expense_details = (category, description, amount)

    expenses[expense_id] = expense_details

    print("EXPENSE ADDED SUCCESSFULLY!")

#Fumnction to display all expenses
def view_expenses():
    print("\n------VIEW ALL EXPENSES------")

    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    for expense_id, details in expenses.items():
        print("\nExpense ID:", expense_id)
        print("Category:", details[0])
        print("Description:", details[1])
        print("Amount: ₹", details[2])

#Function to calculate whole expenses
def total_expenses():
    total = 0

    for details in expenses.values():
        total += details[2]

    print("\nTotal Expenses: ₹", total)

#Functions for Category wise summary
def category_summary():
    print("\n------CATEGORY WISE SUMMARY------")

    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return 
    summary = {}

    for details in expenses.values():
        category = details[0]
        amount = details[2]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    for category, total in summary.items():
        print(category, ": ₹", total)

#Function to search for an expense by ID
def search_expense():
    print("\n------SEARCH EXPENSE BY ID------")

    expense_id = input("Enter the expense ID to search: ")
    if expense_id in expenses:
        details = expenses[expense_id]
        print("\nExpense ID:", expense_id)
        print("Category:", details[0])
        print("Description:", details[1])
        print("Amount: ₹", details[2])
    else:
        print("Expense ID not found.")

#Function to delete an expense by ID
def delete_expense():
    print("\n------DELETE EXPENSE BY ID------")

    expense_id = input("Enter the expense ID to delete: ")

    if expense_id in expenses:
        del expenses[expense_id]
        print("Expense deleted successfully.")
    else:
        print("Expense ID not found.")

#MAIN FUNCTION 
def main():

    while True:

        print("\n-------PERSONAL EXPENSE TRACKER--------")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Expenses")
        print("4. Category Wise Summary")
        print("5. Search Expense by ID")
        print("6. Delete Expense by ID")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            category_summary()
            
        elif choice == "5":
            search_expense()

        elif choice == "6":
            delete_expense()

        elif choice == "7":
            print("Thank you for using the Personal Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")

#CALLING THE MAIN FUNCTION TO START THE PROGRAM:
main()
