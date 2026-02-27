library = {
    "B001": {"title": "The Alchemist","author": "Paulo Coelho","year": 1988,"copies": 4},
    "B002": {"title": "Atomic Habits","author": "James Clear","year": 2018,"copies": 3},
    "B003": {"title": "Rich Dad Poor Dad","author": "Robert Kiyosaki","year": 1997,"copies": 5},
    "B004": {"title": "Introduction to Algorithms","author": "Thomas H. Cormen","year": 2009,"copies": 2},
    "B005": {"title": "Clean Code","author": "Robert C. Martin","year": 2008,"copies": 3}
}


class BookList:
    def __init__(self,title,author,copies):
        self.title = title
        self.author = author
        self.copies = copies

    def view_books(self):
        for book in library.values():
            return book

    def borrow_book(self):
        for book in library.values():
            if book["title"] == self.title:
                if book["copies"] > 0:
                    book["copies"] -= 1
                    return "Book is issued."
        return "Book not found!."

    def return_book(self):
        for book in library.values():
            if book["title"] == self.title:
                if book["copies"] > 0:
                    book["copies"] += 1
                    return "Book return successfully."
        return "Book not found!."

title = "The Alchemist"
author = "Paulo Coelho" 
copies = 4
B = BookList(title,author,copies)
print(B.view_books())
print(B.borrow_book())
print(B.return_book())