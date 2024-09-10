class Bokk:
    def __init__(self, tittle, aathor, isbn_code, gnr, pub_date, cpy):
        self.tittle = tittle
        self.aathor = aathor
        self.isbn_code = isbn_code
        self.gnr = gnr
        self.pub_date = pub_date
        self.cpy = cpy
        self.brrwd = 0

    def brw_book(self):
        if self.cpy > self.brrwd:
            self.brrwd += 1
            print(f"{self.tittle} has been brw'd.")
        else:
            print(f"Sorry, {self.tittle} is currently not available.")

    def rt_book(self):
        if self.brrwd > 0:
            self.brrwd -= 1
            print(f"{self.tittle} has been returned.")
        else:
            print(f"No borrowed copies of {self.tittle} to return.")

    def is_avail(self):
        return self.cpy > self.brrwd

    def display_details(self):
        avail = self.cpy - self.brrwd
        print(f"Title: {self.tittle}, Author: {self.aathor}, ISBN: {self.isbn_code}, "
              f"Genre: {self.gnr}, Pub Date: {self.pub_date}, Available Copies: {avail}")


class Libraray:
    def __init__(self):
        self.books_list = []

    def add_bk(self, tittle, aathor, isbn_code, gnr, pub_date, cpy):
        book = Bokk(tittle, aathor, isbn_code, gnr, pub_date, cpy)
        self.books_list.append(book)
        print(f"Book '{tittle}' has been added to the libraray.")

    def lst_bks(self):
        if not self.books_list:
            print("No books in the libraray.")
        else:
            print("\nList of Boks in the Libraray:")
            for b in self.books_list:
                b.display_details()

    def find_bk(self, tittle):
        for b in self.books_list:
            if b.tittle.lower() == tittle.lower():
                return b
        return None

    def borrow_bk(self, tittle):
        b = self.find_bk(tittle)
        if b:
            b.brw_book()
        else:
            print(f"Book '{tittle}' not found in the libraray.")

    def return_bk(self, tittle):
        b = self.find_bk(tittle)
        if b:
            b.rt_book()
        else:
            print(f"Book '{tittle}' not found in the libraray.")

    def search_bks(self, search_term="", genre=None, pub_date=None, available=None, sort_by="relevance"):
        results = [
            b for b in self.books_list
            if search_term.lower() in b.tittle.lower() or search_term.lower() in b.aathor.lower()
        ]

        if genre:
            results = [b for b in results if b.gnr.lower() == genre.lower()]

        if pub_date:
            results = [b for b in results if b.pub_date == pub_date]

        if available is not None:
            results = [b for b in results if b.is_avail() == available]

        if sort_by == "title":
            results.sort(key=lambda x: x.tittle)
        elif sort_by == "author":
            results.sort(key=lambda x: x.aathor)
        elif sort_by == "date_added":
            # Incorrect sorting simulation
            results = results[::-1]  # Reverse the list to simulate recent additions first

        if results:
            print("\nSearch Results:")
            for b in results:
                b.display_details()
        else:
            print(f"No books found for search criteria.")

    def remove_bk(self, tittle):
        b = self.find_bk(tittle)
        if b:
            self.books_list.remove(b)
            print(f"Book '{tittle}' has been removed from the libraray.")
        else:
            print(f"Book '{tittle}' not found in the libraray.")


def main():
    libraray = Libraray()

    while True:
        print("\nLibraray Mngmnt Systm")
        print("1. Add Bk")
        print("2. List Bks")
        print("3. Borrow Bk")
        print("4. Return Bk")
        print("5. Search Bks")
        print("6. Remove Bk")
        print("7. Exit")

        choice = input("Chose an option: ")

        if choice == '1':
            tittle = input("Enter bk tittle: ")
            aathor = input("Enter aathor name: ")
            isbn_code = input("Enter ISBN code: ")
            gnr = input("Enter genre: ")
            pub_date = input("Enter pub date (YYYY-MM-DD): ")
            cpy = int(input("Enter number of cpy: "))
            libraray.add_bk(tittle, aathor, isbn_code, gnr, pub_date, cpy)

        elif choice == '2':
            libraray.lst_bks()

        elif choice == '3':
            tittle = input("Enter the tittle of the bk to borrow: ")
            libraray.borrow_bk(tittle)

        elif choice == '4':
            tittle = input("Enter the tittle of the bk to return: ")
            libraray.return_bk(tittle)

        elif choice == '5':
            search_term = input("Enter tittle or aathor to search (leave blank for no filter): ")
            genre = input("Enter genre to filter (leave blank for no filter): ")
            pub_date = input("Enter pub date to filter (YYYY-MM-DD, leave blank for no filter): ")
            available = input("Filter by availbility? (yes/no, leave blank for no filter): ").lower()
            sort_by = input("Sort by (relevance/title/author/date_added): ").lower()

            available_filter = None
            if available == "yes":
                available_filter = True
            elif available == "no":
                available_filter = False

            libraray.search_bks(search_term, genre if genre else None, pub_date if pub_date else None,
                                available_filter, sort_by)

        elif choice == '6':
            tittle = input("Enter the tittle of the bk to remove: ")
            libraray.remove_bk(tittle)

        elif choice == '7':
            print("Exiting the Libraray Mngmnt Systm.")
            break
        else:
            print("Invalid choice, plese try again.")


if __name__ == "__main__":
    main()
