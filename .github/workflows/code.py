import datetime

print("Welcome to Your Personal Finance Manager!")
print("You can track expenses, income, and savings here. Let's get started!")

records = {
    "expenses": [],
    "income": [],
    "savings": []
}

def today():
    return datetime.date.today().isoformat()

def add_finance_data():
    entry_type_map = {
        "E": "expenses",
        "I": "income",
        "S": "savings"
    }

    choice = input("Enter type (E = Expense, I = Income, S = Savings): ").strip().upper()
    if choice in entry_type_map:
        entry_type = entry_type_map[choice]
        try:
            amount = float(input(f"Enter {entry_type} amount: "))
            category = input(f"Enter {entry_type} category: ")
            date = input("Enter date (DD-MM-YYYY) or press Enter for today: ") or today()

            records[entry_type].append({
                "amount": amount,
                "category": category,
                "date": date
            })
            print(f"{entry_type.capitalize()} of {amount} added successfully.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number for amount.\n")
    else:
        print("Invalid choice. Use E, I, or S.\n")

def calculate_totals():
    totals = {
        "expenses": sum(entry["amount"] for entry in records["expenses"]),
        "income": sum(entry["amount"] for entry in records["income"]),
        "savings": sum(entry["amount"] for entry in records["savings"])
    }
    return totals

def show_summary():
        totals = calculate_totals()
        net_savings = totals["income"] - totals["expenses"]
        print("\n Monthly Summary:")
        print(f"Total Income   : {totals['income']}")
        print(f"Total Expenses : {totals['expenses']}")
        print(f"Total Savings  : {totals['savings']}")
        print(f"Net Savings    : {net_savings}\n")

def calculate_totals():
        return {
            "expenses": sum(entry["amount"] for entry in records["expenses"]),
            "income": sum(entry["amount"] for entry in records["income"]),
            "savings": sum(entry["amount"] for entry in records["savings"])
        }
        
def view_entries():
    print("\n All Financial Entries:")
    for key, entries in records.items():
        print(f"\n{key.capitalize()}:")
        if entries:
            for entry in entries:
                print(f"  - {entry['date']} | {entry['category'].title()} | {entry['amount']}")
        else:
            print("  No entries yet.")
    print()

def reset_data():
    confirm = input("Reset all data? (y/n): ").strip().lower()
    if confirm == "y":
        for key in records:
            records[key].clear()
        print("✅ All data has been reset.\n")
    else:
        print("❌ Reset cancelled.\n")

def main_menu():
    while True:
        print("Select an option:")
        print("1. Add Financial Entry (E/I/S)")
        print("2. View Monthly Summary")
        print("3. View All Entries")
        print("4. Reset All Data")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_finance_data()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            view_entries()
        elif choice == "4":
            reset_data()
        elif choice == "0":
            print("Thank you for using Finance Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
main_menu()
