# PERSONAL-BUDGET-TRACKER

## Overview
This is a Python-based command-line budget tracker application that helps users manage their financial transactions. The application allows users to record income and expenses, view their transactions, calculate the remaining budget, analyze expenses by category, and exit the application. Transaction details, including category, amount, and date, are stored in a JSON file for future reference.

## Getting Started
To use the budget tracker application, follow these steps:

1. Clone or download the repository.
2. Ensure that you have Python installed on your system.
3. Run the `budget_tracker.py` file using the command `python budget_tracker.py` in your terminal.

## Commands
The application provides the following commands in the command menu:

1. **Display Transactions:** View a summary of income and expenses, including their respective categories, amounts, and dates.
2. **Add Income:** Add a new income entry by specifying the category and amount.
3. **Add Expense:** Add a new expense entry by specifying the category and amount.
4. **Calculate Budget:** Calculate and display the remaining budget based on recorded income and expenses.
5. **Analyze Expenses:** View an analysis of expenses, showing the total amount spent in each expense category.
6. **Exit:** Save transactions and exit the application.

## Transaction Structure
Each transaction includes the following details:

- **Category:** The category of the income or expense.
- **Amount:** The amount of money associated with the transaction.
- **Date:** The date and time when the transaction was recorded.

## Data Storage
Transaction data is stored in a JSON file named `transactions.json`. The file is created automatically and is updated as new income and expense entries are added.

## Notes
- Amounts for income and expenses should be entered as numerical values.
- The application will continue running until the user chooses to exit.

Feel free to customize and enhance this budget tracker application based on your financial tracking needs!
