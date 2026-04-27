import csv
import os

FILE = "expenses.csv"

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([amount, category])

    print("Expense added successfully!")

def view_expenses():
    if not os.path.exists(FILE):
        print("No expenses found.")
        return

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(f"Amount: {row[0]}, Category: {row[1]}")

def total_expense():
    total = 0
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                total += float(row[0])

    print(f"Total Expense: {total}")

def main():
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Total Expense\n4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
