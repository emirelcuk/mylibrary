class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        self.borrowed = 0

    def borrow_book(self):
        if self.copies > self.borrowed:
            self.borrowed += 1
            print(f"{self.title} has been borrowed.")
        else:
            print(f"Sorry, {self.title} is currently not available.")

    def return_book(self):
        if self.borrowed > 0:
            self.borrowed -= 1
            print(f"{self.title} has been returned.")
        else:
            print(f"No borrowed copies of {self.title} to return.")

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
        book = self.find_book(title)
        if book:
            book.borrow_book()
        else:
            print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        book = self.find_book(title)
        if book:
            book.return_book()
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
        book = self.find_book(title)
        if book:
            self.books.remove(book)
            print(f"Book '{title}' has been removed from the library.")
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
        print("5. Search Book")
        print("6. Remove Book")
        print("7. Exit")

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
            library.borrow_book(title)

        elif choice == '4':
            title = input("Enter the title of the book to return: ")
            library.return_book(title)

        elif choice == '5':
            search_term = input("Enter title or author to search: ")
            library.search_books(search_term)

        elif choice == '6':
            title = input("Enter the title of the book to remove: ")
            library.remove_book(title)

        elif choice == '7':
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
