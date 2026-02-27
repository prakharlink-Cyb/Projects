items = {
    "aata" : 50,
    "biskit" : 5,
    "besan" : 50,
    "chips" : 5,
    "cookie" : 20,
    "choclket" : 10,
    "megi" : 20,
}
shopping_items = []


while True: 
    order = input("Enter your items(or 'Done' for exit): ")
    
    if order == "Done":
        print("Total amount:- ",sum(shopping_items))
        break 

    elif order in items:
        shopping_items.append(items[order])
        print(order,"added")

    else:
        print("Item not in storage.")
