class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        self.borrowed = 0
        self.reserved_by = []  # List to keep track of users who reserved the book

    def borrow_book(self, member):
        if self.copies > self.borrowed:
            self.borrowed += 1
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


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn, copies):
        book = Book(title, author, isbn, copies)
        self.books.append(book)
        print(f"Book '{title}' has been added to the library.")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, title, member):
        book = self.find_book(title)
        if book:
            book.borrow_book(member)
        else:
            print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        book = self.find_book(title)
        if book:
            book.return_book()
        else:
            print(f"Book '{title}' not found in the library.")

    def reserve_book(self, title, member):
        book = self.find_book(title)
        if book:
            book.reserve_book(member)
        else:
            print(f"Book '{title}' not found in the library.")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Reserve Book")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN number: ")
            copies = int(input("Enter number of copies: "))
            library.add_book(title, author, isbn, copies)

        elif choice == '2':
            library.list_books()

        elif choice == '3':
            title = input("Enter the title of the book to borrow: ")
            member = input("Enter member name: ")
            library.borrow_book(title, member)

        elif choice == '4':
            title = input("Enter the title of the book to return: ")
            library.return_book(title)

        elif choice == '5':
            title = input("Enter the title of the book to reserve: ")
            member = input("Enter member name: ")
            library.reserve_book(title, member)

        elif choice == '6':
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
