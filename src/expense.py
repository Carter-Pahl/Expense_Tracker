from dateutil.parser import parse
from . import categories

class Expense:
    def __init__(self, amount, category, date, ):
        self.amount = amount
        self.category = category
        self.date = date

    def __str__(self):
        return f"Amount: {self.amount} /n Category: {self.category} /n Date: {self.date}"

    @classmethod
    def get(cls):
        return cls(input("Amount: "), input("Category: "), input("Date: "), )

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        try:
            val = float(value)
        except ValueError:
            raise ValueError("Amount must be a number")
        if val <= 0:
            raise ValueError("Amount must be positive")
        self._amount = val
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if value not in categories.load_categories():
            raise ValueError("Invalid category")
        self._category = value

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        try:
            parsed_date = parse(value).date()
            self._date = parsed_date
        except ValueError:
            raise ValueError("Could not parse date. Please try a different format.")


