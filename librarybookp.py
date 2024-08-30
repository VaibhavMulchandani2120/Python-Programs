class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book}' has been added to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"'{book}' has been removed from the library.")
        else:
            print(f"'{book}' is not in the library.")

    def display_books(self):
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("The library is empty.")

# Test the class
library = Library()
library.add_book("The Catcher in the Rye")
library.add_book("To Kill a Mockingbird")
library.display_books()
library.remove_book("To Kill a Mockingbird")
library.display_books()
