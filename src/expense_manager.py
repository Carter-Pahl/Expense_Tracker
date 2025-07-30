from pathlib import Path
import csv
from datetime import datetime
from .expense import Expense

expense_file = Path("../data/expenses.csv")

class ExpenseManager:
    def __init__(self):
        self.expenses = []
    
    def add_expense(self, expense):
        self.expenses.append(expense)
    
    def save_to_file(self):
        expense_file.parent.mkdir(exist_ok=True)

        with open(expense_file, "a", newline="") as f:
            writer = csv.writer(f)
            if not expense_file.exists():
                writer.writerow(["date", "category", "amount"])
            for exp in self.expenses:
                writer.writerow[exp.date.isoformat(), exp.category, exp.amount]
        
        self.expenses = []
    
    def load_from_file(self):
        if not expense_file.exists():
            return
        
        with open(expense_file, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    expense = Expense(
                    amount=row["amount"],
                    date=row["date"],
                    category=row["category"]
                    )
                    
                    self.expenses.append(expense)
                except ValueError as e:
                    print(f"Skipping invalid row. Reason: {e}")

    def report_by_category(self, category):
        totals = {}
        for exp in self.expenses:
            totals[exp.category] = totals.get(exp.category, 0) + exp.amount
        return totals
    
    # def report_by_date_range(self):