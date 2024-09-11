class Book:
    def __init__(self, title, author, isbn, genre, publication_date, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publication_date = publication_date
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

    def is_available(self):
        return self.copies > self.borrowed

    def display_info(self):
        available = self.copies - self.borrowed
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, "
              f"Genre: {self.genre}, Publication Date: {self.publication_date}, "
              f"Available Copies: {available}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn, genre, publication_date, copies):
        book = Book(title, author, isbn, genre, publication_date, copies)
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

    def search_books(self, search_term="", genre=None, publication_date=None, available=None, sort_by="relevance"):
        results = [
            book for book in self.books
            if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower()
        ]

        if genre:
            results = [book for book in results if book.genre.lower() == genre.lower()]

        if publication_date:
            results = [book for book in results if book.publication_date == publication_date]

        if available is not None:
            results = [book for book in results if book.is_available() == available]

        if sort_by == "title":
            results.sort(key=lambda x: x.title)
        elif sort_by == "author":
            results.sort(key=lambda x: x.author)
        elif sort_by == "date_added":
            # Assuming books are added in order, this simulates sorting by date added
            results = results[::-1]  # Reverse the list to simulate recent additions first

        if results:
            print("\nSearch Results:")
            for book in results:
                book.display_info()
        else:
            print(f"No books found for search criteria.")

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
        print("5. Search Books")
        print("6. Remove Book")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN number: ")
            genre = input("Enter genre: ")
            publication_date = input("Enter publication date (YYYY-MM-DD): ")
            copies = int(input("Enter number of copies: "))
            library.add_book(title, author, isbn, genre, publication_date, copies)

        elif choice == '2':
            library.list_books()

        elif choice == '3':
            title = input("Enter the title of the book to borrow: ")
            library.borrow_book(title)

        elif choice == '4':
            title = input("Enter the title of the book to return: ")
            library.return_book(title)

        elif choice == '5':
            search_term = input("Enter title or author to search (leave blank for no filter): ")
            genre = input("Enter genre to filter (leave blank for no filter): ")
            publication_date = input("Enter publication date to filter (YYYY-MM-DD, leave blank for no filter): ")
            available = input("Filter by availability? (yes/no, leave blank for no filter): ").lower()
            sort_by = input("Sort by (relevance/title/author/date_added): ").lower()

            available_filter = None
            if available == "yes":
                available_filter = True
            elif available == "no":
                available_filter = False

            library.search_books(search_term, genre if genre else None, publication_date if publication_date else None,
                                 available_filter, sort_by)

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
