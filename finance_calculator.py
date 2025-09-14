# Ask the user for their monthly income
income = float(input("How much money do you earn each month? "))

# Ask the user for their monthly expenses
expenses = float(input("How much do you spend each month? "))

# Calculate how much money is left after expenses
monthly_savings = income - expenses

# Calculate yearly savings (12 months)
annual_savings = monthly_savings * 12

# Add 5% interest to the yearly savings
interest = annual_savings * 0.05
projected_savings = annual_savings + interest

# Show the results with friendly messages
print(f"\nYou save ${monthly_savings:.2f} every month.")
print(f"After one year, with 5% interest, you'll have about ${projected_savings:.2f} saved.")
