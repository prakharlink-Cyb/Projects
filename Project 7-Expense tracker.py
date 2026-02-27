expenses = []

def Add_expens():
    amount = float(input("Enter amound: "))
    item = input("Enter item name: ")

    Expens = {
        "amount" : amount,
        "item" : item
    }

    expenses.append(Expens)


def View_expens():
    if not expenses:
        print("NO item in the list.")
    else:
        for exp in expenses:
            print(exp)

def Calculate_Total_Expense():
    if not expenses:
        print("No expenses found")
        return
    total = 0 
    for exp in expenses:
        total += exp["amount"]

    print("Total expense: ",total)

def Save_to_file():
    try:
        with open('Project/Expenses.txt','r') as file:
            for line in file:
                amount,item = line.strip().split(",")
                expenses.append({
                    "amount" : amount,
                    "item" : item
                })
                print("Expenses loaded from file.\n")

    except FileNotFoundError:
        print("No saved file found.\n")


while True:
    print("---- Expense Tracker ----")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Save Expenses")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        Add_expens()
    elif choice == "2":
        View_expens()
    elif choice == "3":
        Calculate_Total_Expense()
    elif choice == "4":
        Save_to_file()
    elif choice == "5":
        Save_to_file()
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")





'''
1.First make empty list.
2.make function 
    amount 
    user item
    append list 
    retun expension

1.Make function
    View one by one all element.
    if Expension is equal to " " 
        print("List is empty.")
    else:
        print all the items from the list.

1.Make function Calculate_Total_Expense
2.read the expension amount from the list. 
        if amount is equal to 0
            it prints there is no item
        else:
            calculate all the amount in the list.
                Then print the total amount

1.make function Save_to_file()
2.Open the file.
    try:
        read line by line content in file:
        in the amount and item there is any space so we remove this and change into commas.
        expenses append in the form of dictionary
        then it print expenses loaded from file.
    except filenotfounderror:
        then print file is not found



'''