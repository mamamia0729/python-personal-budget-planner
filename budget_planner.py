# Personal Budget Planner
# A simple tool to calculate monthly budget and provide financial advice

print("Welcome to the Personal Budget Planner!")
print("Please enter numbers only (e.g., 1000.50).")

# Get income
income = float(input("Enter your monthly income: $"))
if income < 0:
    print("Warning: Income cannot be negative. Using $0 instead.")
    income = 0

# Get rent
rent = float(input("Enter your monthly rent: $"))
if rent < 0:
    print("Warning: Rent cannot be negative. Using $0 instead.")
    rent = 0

# Get groceries
groceries = float(input("Enter your monthly grocery expenses: $"))
if groceries < 0:
    print("Warning: Groceries cannot be negative. Using $0 instead.")
    groceries = 0

# Get utilities
utilities = float(input("Enter your monthly utilities expenses: $"))
if utilities < 0:
    print("Warning: Utilities cannot be negative. Using $0 instead.")
    utilities = 0

# Get entertainment
entertainment = float(input("Enter your monthly entertainment expenses: $"))
if entertainment < 0:
    print("Warning: Entertainment cannot be negative. Using $0 instead.")
    entertainment = 0

# Calculate total expenses and remaining balance
total_expenses = rent + groceries + utilities + entertainment
balance = income - total_expenses

# Display budget summary
print("\n=== Budget Summary ===")
print("Monthly Income: $" + str(round(income, 2)))
print("Total Expenses: $" + str(round(total_expenses, 2)))
print("Remaining Balance: $" + str(round(balance, 2)))

# Provide financial advice based on balance
if balance > 500:
    print("Financial Status: Surplus")
    print("Great job! You have extra money. Consider saving some.")
elif balance > 0:
    print("Financial Status: Balanced")
    print("You're doing okay! Try to save a little if you can.")
elif balance == 0:
    print("Financial Status: Neutral")
    print("You spent exactly what you earned. Be careful next month.")
else:
    print("Financial Status: Deficit")
    print("Warning: You're spending too much. Try to cut back.")
