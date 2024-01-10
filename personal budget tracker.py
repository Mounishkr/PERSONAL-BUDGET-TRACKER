import os
import json
from datetime import datetime

# File to store transactions
TRANSACTIONS_FILE = "transactions.json"

def load_transactions():
    if os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, "r") as file:
            transactions = json.load(file)
        return transactions
    else:
        return {"income": [], "expenses": []}

def save_transactions(transactions):
    with open(TRANSACTIONS_FILE, "w") as file:
        json.dump(transactions, file, indent=2)

def display_transactions(income, expenses):
    print("\nIncome:")
    for entry in income:
        print(f"{entry['category']}: +${entry['amount']} ({entry['date']})")

    print("\nExpenses:")
    for entry in expenses:
        print(f"{entry['category']}: -${entry['amount']} ({entry['date']})")

def add_income(transactions, category, amount):
    transactions["income"].append({"category": category, "amount": amount, "date": str(datetime.now())})
    print("Income entry added successfully.")

def add_expense(transactions, category, amount):
    transactions["expenses"].append({"category": category, "amount": amount, "date": str(datetime.now())})
    print("Expense entry added successfully.")

def calculate_budget(transactions):
    total_income = sum(entry["amount"] for entry in transactions["income"])
    total_expenses = sum(entry["amount"] for entry in transactions["expenses"])
    remaining_budget = total_income - total_expenses
    return remaining_budget

def analyze_expenses(transactions):
    expense_categories = {}
    for entry in transactions["expenses"]:
        category = entry["category"]
        amount = entry["amount"]
        if category in expense_categories:
            expense_categories[category] += amount
        else:
            expense_categories[category] = amount
    return expense_categories

def main():
    transactions = load_transactions()

    while True:
        print("\nCommand Menu:")
        print("1. Display Transactions")
        print("2. Add Income")
        print("3. Add Expense")
        print("4. Calculate Budget")
        print("5. Analyze Expenses")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            display_transactions(transactions["income"], transactions["expenses"])
        elif choice == "2":
            category = input("Enter income category: ")
            amount = float(input("Enter income amount: "))
            add_income(transactions, category, amount)
        elif choice == "3":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            add_expense(transactions, category, amount)
        elif choice == "4":
            remaining_budget = calculate_budget(transactions)
            print(f"Remaining Budget: ${remaining_budget}")
        elif choice == "5":
            expense_categories = analyze_expenses(transactions)
            print("\nExpense Analysis:")
            for category, amount in expense_categories.items():
                print(f"{category}: ${amount}")
        elif choice == "6":
            save_transactions(transactions)
            print("Exiting the budget tracker application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
