monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses:"))
monthly_savings = monthly_income - monthly_expenses
annual_intrest_rate = 0.05
print(monthly_savings * 12 + (monthly_savings * 12 * 0.05))