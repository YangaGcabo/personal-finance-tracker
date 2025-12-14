from dataclasses import dataclass
from datetime import date

@dataclass
class Transaction:
    amount: float
    category: str
    transaction_date: date
