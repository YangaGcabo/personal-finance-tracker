def monthly_balance(transactions):
    income = sum(t.amount for t in transactions if t.amount > 0)
    expense = sum(t.amount for t in transactions if t.amount < 0)
    return income + expense
