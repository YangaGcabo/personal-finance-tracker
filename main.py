import pandas as pd

data = {
    "date": ["2025-01-01", "2025-01-05", "2025-01-10"],
    "description": ["Salary", "Groceries", "Transport"],
    "amount": [15000, -1200, -500],
}

df = pd.DataFrame(data)
df["balance"] = df["amount"].cumsum()

print("Personal Finance Summary:")
print(df)
