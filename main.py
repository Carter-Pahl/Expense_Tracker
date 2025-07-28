from src.expense import Expense
import src.categories
import csv

def main():
    # Prompts user to select an option and catches any errors
    while True:
        try: 
            option = int(input("Select a number: \n1) Add an expense \n2) See expenses per category \n3) See expenses by date range \n4) Edit Categories \n5) Quit \n"))
            if option not in [1, 2, 3, 4, 5]:
                raise ValueError
            break
        except ValueError:
            print("\n**Please enter an integer from 1-4**\n")

    #Prompts user to fill out expense fields and passes in valid categories
    if option == 1:
        valid_categories = src.categories.load_categories()
        with open(src.expenses.csv, "a") as file:
                file.write(Expense.get(valid_categories))
    
    # #Lists expenses of a given category
    # if option == 2:

    # #Lists expenses of a specified date range
    # if option == 3:

    #Edit category sequence (view categories, add categories, remove categories)
    if option == 4:
        print("Here are your current categories:")
        print(*src.categories.load_categories(), sep="\n")
        try:
            option_2 = int(input("\nSelect a number: \n1) Add a category \n2) Delete a category \n"))
            if option_2 not in [1, 2]: raise ValueError
        except ValueError:
            print("\n**Please enter an integer from 1-2**")
        if option_2 == 1: src.categories.add_category(input("Input new category: \n")) #Adds a new category
        if option_2 == 2: src.categories.delete_category(input("Input the category you would like to delete: \n")) #Deletes an existing category




if __name__ == "__main__":
    main()