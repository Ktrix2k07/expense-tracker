expenses = []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View category totals")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = input("Amount: ")
        category = input("Category: ")

        expense = {
            "amount": amount,
            "category": category
        }

        expenses.append(expense)
        print("Expense added!")

    elif choice == "2":
        if not expenses:
            print("No expenses added yet.")
        else:
            for expense in expenses:
                print(f"{expense['category']}: ₹{expense['amount']}")

    elif choice == "3":
        totals = {}

        for expense in expenses:
            category = expense["category"]
            amount = float(expense["amount"])

            if category in totals:
                totals[category] += amount
            else:
                totals[category] = amount

        print("\n--- Category Totals ---")
        for category, total in totals.items():
            print(f"{category}: ₹{total}")

    elif choice == "4":
        print("Exiting the program.")
        break

    else:
        print("Please choose 1, 2, 3, or 4.")