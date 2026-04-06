import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

# Initialize file if not exists
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category"])

# Add expense
def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category (Food, Travel, etc.): ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category])

    print("✅ Expense added successfully!\n")

# View all expenses
def view_expenses():
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header

            print("\n📋 All Expenses:")
            for row in reader:
                print(f"Date: {row[0]}, Amount: ₹{row[1]}, Category: {row[2]}")
            print()
    except FileNotFoundError:
        print("No expenses found.\n")

# Show summary
def show_summary():
    summary = {}

    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                category = row[2]
                amount = float(row[1])

                if category in summary:
                    summary[category] += amount
                else:
                    summary[category] = amount

        print("\n📊 Expense Summary:")
        total = 0
        for category, amount in summary.items():
            print(f"{category}: ₹{amount}")
            total += amount

        print(f"\n💰 Total Spending: ₹{total}\n")

    except FileNotFoundError:
        print("No data available.\n")

# Main menu
def main():
    init_file()

    while True:
        print("==== Smart Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            show_summary()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.\n")

if __name__ == "__main__":
    main()