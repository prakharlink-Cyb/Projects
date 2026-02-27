contact_book = {
    "Prakhar": "3265132132",
    "Pranav": "4561321665",
    "Somya": "3216549876"
}

class Contact:
    def __init__(self, name, number=None):
        self.name = name
        self.number = number

    def add_contact(self):
        if self.name in contact_book:
            return "Contact already exists"
        else:
            contact_book[self.name] = self.number
            return "Contact added successfully"

    def get_number(self):
        if self.name in contact_book:
            return contact_book[self.name]
        else:
            return "Contact not found"


# -------- Main Program --------
choice = input("Enter 1 to add contact, 2 to search contact: ")

if choice == "1":
    name = input("Enter name: ")
    number = input("Enter number: ")
    c = Contact(name, number)
    print(c.add_contact())

elif choice == "2":
    name = input("Enter name: ")
    c = Contact(name)
    print(c.get_number())

else:
    print("Invalid choice")
