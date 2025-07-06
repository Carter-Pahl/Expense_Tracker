**Goal:**
Build a **command-line expense tracker** that lets a user:

* Add expenses with a category, amount, and date
* Save expenses to a CSV file
* Load and display total spending per category
* Show total expenses for a given month or date range
* Use OOP for expense records and the manager
* Add unit tests for your methods
* Use Git and a clear project structure

---

## 📌 **Project Description**

**Your app should do this:**

1️⃣ **Add an expense**

* Ask the user for: *date* (ISO format `YYYY-MM-DD`), *category* (like `"Groceries"`), and *amount*.
* Validate input: date must be valid, amount must be positive.

2️⃣ **Save expenses**

* Each expense is saved to a `expenses.csv` file.
* If the file doesn’t exist, create it with headers: `date,category,amount`.

3️⃣ **Load expenses**

* On start, load all expenses from `expenses.csv` into a list of `Expense` objects.

4️⃣ **Report**

* Calculate and print total spending by category.
* Calculate total spending for a given month or date range.

5️⃣ **OOP structure**

* `Expense` class → represents one expense.
* `ExpenseManager` class → holds a list of expenses and has methods for:

  * `add_expense()`
  * `save_to_file()`
  * `load_from_file()`
  * `report_by_category()`
  * `report_by_date_range()`

6️⃣ **Unit tests**

* Use `pytest` in a `tests/` folder.
* Test adding an expense.
* Test loading from file.
* Test reports return correct totals.

7️⃣ **CLI**

* Have a `main.py` with an `if __name__ == "__main__":` that:

  * Loads expenses.
  * Shows a menu:
    1. Add expense
    2. Show total by category
    3. Show total by date range
    4. Quit
  * Calls your methods accordingly.

8️⃣ **Project structure**

```
expense_tracker/
├── pyproject.toml (or requirements.txt)
├── .gitignore
├── README.md
├── src/
│   └── expense_tracker/
│       ├── __init__.py
│       ├── manager.py
│       └── models.py
├── tests/
│   └── test_manager.py
├── data/
│   └── expenses.csv
└── main.py
