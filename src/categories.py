from pathlib import Path

categories_file = Path("data/categories.txt")


def load_categories():
    with open(categories_file, "r") as file:
        if not categories_file.exists():
            return []
        else:
            return [line.strip() for line in file if line.strip()]

def add_category(value):
    categories = set(load_categories())
    if value not in categories:
        with open(categories_file, "a") as file:
            file.write(f"{value}\n")
        print("Category has been added")
    else:
        print("This category already exists")

def delete_category(value):
    categories = set(load_categories())
    if value in categories:
        categories.remove(value)
        with open(categories_file, "w") as file:
            for category in categories:
                file.write(f"{category}\n")
        print("Category has been deleted")
    else:
        print("This category doesn't exist")
    