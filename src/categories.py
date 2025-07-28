from pathlib import Path

categories_file = Path("data/categories.txt")


def load_categories():
    with open(categories_file, "r") as file:
        if not categories_file.exists:
            return []
        else:
            return [line.strip() for line in f if line.strip()]

def add_category(value):
    categories = set(load_categories)
    if value not in categories
        with open(categories_file, "a") as file:
            file.write(f"{value}\n")