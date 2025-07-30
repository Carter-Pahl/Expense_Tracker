from src.expense import Expense
import src.categories
from src.expense_manager import ExpenseManager

def main():
    while True:
        option = get_user_option(
            prompt="1) Add an expense \n2) See expenses per category \n3) See expenses by date range \n4) Edit categories \n5) Quit \n",
            valid_options=[1,2,3,4,5])
        if option == 1: option_1()
        if option == 2: option_2()
        # if option == 3: option_3()
        if option == 4: option_4()
        if option == 5: break
        

def option_1():
    manager = ExpenseManager()
    while True:
            manager.add_expense(Expense.get())
            option_2 = get_user_option(
            prompt="1) Add another expense \n2) Save expenses and quit",
            valid_options=[1,2])
            if option_2 ==2:
                manager.save_to_file()
                break

def option_2():
    manager = ExpenseManager()
    manager.load_from_file()
    totals = manager.report_by_category()
    for category, amount in totals.items():
        print(f"{category}: ${amount:.2f}")


# def option_3():

def option_4():
    print("Here are your current categories:")
    print(*src.categories.load_categories(), sep="\n")

    option_3 = get_user_option(
    prompt="1) Add a category \n2) Delete a category \n",
    valid_options=[1,2])
    if option_3 == 1: src.categories.add_category(input("New category: \n"))
    if option_3 == 2: src.categories.delete_category(input("Category to delete: \n"))

def get_user_option(prompt, valid_options):
    while True:
        try:
            option = int(input(prompt))
            if option not in valid_options: raise ValueError
            return option
        except ValueError:
            print(f"\n**Please enter an integer from {valid_options[0]}-{valid_options[-1]}**\n")


if __name__ == "__main__":
    main()