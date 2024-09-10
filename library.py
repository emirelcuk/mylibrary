class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        self.borrowed = 0
        self.reserved_by = []  # List to keep track of users who reserved the book

    def borrow_book(self):
    def borrow_book(self, member):
        if self.copies > self.borrowed:
            self.borrowed += 1
            print(f"{self.title} has been borrowed.")
            print(f"{self.title} has been borrowed by {member}.")
            self.notify_next_reserver()
        else:
            print(f"Sorry, {self.title} is currently not available.")
            self.reserve_book(member)

    def return_book(self):
        if self.borrowed > 0:
            self.borrowed -= 1
            print(f"{self.title} has been returned.")
            self.notify_next_reserver()
        else:
            print(f"No borrowed copies of {self.title} to return.")

    def reserve_book(self, member):
        if member not in self.reserved_by:
            self.reserved_by.append(member)
            print(f"{member} has reserved {self.title}.")
        else:
            print(f"{member} has already reserved {self.title}.")

    def notify_next_reserver(self):
        if self.reserved_by and self.copies > self.borrowed:
            next_member = self.reserved_by.pop(0)
            print(f"Notification: {next_member}, your reserved book '{self.title}' is now available!")

    def display_info(self):
        available = self.copies - self.borrowed
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available Copies: {available}")
@@ -34,24 +50,16 @@ def add_book(self, title, author, isbn, copies):
        self.books.append(book)
        print(f"Book '{title}' has been added to the library.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nList of Books in the Library:")
            for book in self.books:
                book.display_info()

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, title):
    def borrow_book(self, title, member):
        book = self.find_book(title)
        if book:
            book.borrow_book()
            book.borrow_book(member)
        else:
            print(f"Book '{title}' not found in the library.")

@@ -62,21 +70,10 @@ def return_book(self, title):
        else:
            print(f"Book '{title}' not found in the library.")

    def search_books(self, search_term):
        results = [book for book in self.books if
                   search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower()]
        if results:
            print("\nSearch Results:")
            for book in results:
                book.display_info()
        else:
            print(f"No books found for search term '{search_term}'.")

    def remove_book(self, title):
    def reserve_book(self, title, member):
        book = self.find_book(title)
        if book:
            self.books.remove(book)
            print(f"Book '{title}' has been removed from the library.")
            book.reserve_book(member)
        else:
            print(f"Book '{title}' not found in the library.")

@@ -90,9 +87,8 @@ def main():
        print("2. List Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Remove Book")
        print("7. Exit")
        print("5. Reserve Book")
        print("6. Exit")

        choice = input("Choose an option: ")

@@ -108,21 +104,19 @@ def main():

        elif choice == '3':
            title = input("Enter the title of the book to borrow: ")
            library.borrow_book(title)
            member = input("Enter member name: ")
            library.borrow_book(title, member)

        elif choice == '4':
            title = input("Enter the title of the book to return: ")
            library.return_book(title)

        elif choice == '5':
            search_term = input("Enter title or author to search: ")
            library.search_books(search_term)
            title = input("Enter the title of the book to reserve: ")
            member = input("Enter member name: ")
            library.reserve_book(title, member)

        elif choice == '6':
            title = input("Enter the title of the book to remove: ")
            library.remove_book(title)

        elif choice == '7':
            print("Exiting the Library Management System.")
            break
        else:
