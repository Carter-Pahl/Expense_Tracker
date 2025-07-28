from expense.py import Expense

def main():
    while True:
        try: 
            option = int(input("Select a number \n1) Add an expense \n2) See expenses per category \n3) See expenses by date range \n4) Quit \n\n Input:  "))
            if option not in [1, 2, 3, 4]:
                raise ValueError
            break
        except ValueError:
            print("\n***Please enter an integer from 1-4***\n")
    # if option == 1:
    
    # if option == 2:
    
    # if option == 3:


if __name__ == "__main__":
    main()