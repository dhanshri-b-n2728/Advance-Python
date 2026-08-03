# Advance-Python

# Library Management System using OOP

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        return f"{self.title} by {self.author} - {status}"


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"Patron: {self.name}, Borrowed: {[book.title for book in self.borrowed_books]}"


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' added successfully.")

    def register_patron(self, name):
        patron = Patron(name)
        self.patrons.append(patron)
        print(f"Patron '{name}' registered successfully.")

    def borrow_book(self, patron_name, book_title):
        patron = next((p for p in self.patrons if p.name == patron_name), None)
        book = next((b for b in self.books if b.title == book_title), None)

        if not patron:
            print("Patron not found.")
            return
        if not book:
            print("Book not found.")
            return
        if book.is_borrowed:
            print(f"Book '{book_title}' is already borrowed.")
            return

        book.is_borrowed = True
        patron.borrowed_books.append(book)
        print(f"'{patron_name}' borrowed '{book_title}'.")

    def return_book(self, patron_name, book_title):
        patron = next((p for p in self.patrons if p.name == patron_name), None)
        if not patron:
            print("Patron not found.")
            return

        book = next((b for b in patron.borrowed_books if b.title == book_title), None)
        if not book:
            print(f"'{patron_name}' has not borrowed '{book_title}'.")
            return

        book.is_borrowed = False
        patron.borrowed_books.remove(book)
        print(f"'{patron_name}' returned '{book_title}'.")

    def show_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def show_patrons(self):
        if not self.patrons:
            print("No patrons registered.")
        else:
            for patron in self.patrons:
                print(patron)


# User Interface
def main():
    library = Library()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Register Patron")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Show All Books")
        print("6. Show All Patrons")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)

        elif choice == "2":
            name = input("Enter patron name: ")
            library.register_patron(name)

        elif choice == "3":
            patron_name = input("Enter patron name: ")
            book_title = input("Enter book title: ")
            library.borrow_book(patron_name, book_title)

        elif choice == "4":
            patron_name = input("Enter patron name: ")
            book_title = input("Enter book title: ")
            library.return_book(patron_name, book_title)

        elif choice == "5":
            library.show_books()

        elif choice == "6":
            library.show_patrons()h

        elif choice == "7":
            print("Exiting Library System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
