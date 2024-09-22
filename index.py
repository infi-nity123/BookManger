class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}"


class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        book = Book(title, author)
        self.books.append(book)
        print("Book added successfully!")

    def find_book(self):
        search_term = input("Enter title to search: ")
        found_books = []
        for book in self.books:
            if search_term.lower() in book.title.lower():
                found_books.append(book)

        if found_books:
            print("Found books:")
            for book in found_books:
                print(book)
        else:
            print("No books found matching your search.")

    def list_all_books(self):
        if self.books:
            print("All books:")
            for book in self.books:
                print(book)
        else:
            print("No books in the collection.")

    def remove_book(self):
        title = input("Enter title of the book to remove: ")
        for i, book in enumerate(self.books):
            if book.title == title:
                del self.books[i]
                print("Book removed successfully!")
                return
        print("Book with the given title not found.")

    def main_menu(self):
        while True:
            print("\nBook Management System")
            print("1. Add Book")
            print("2. Find Book")
            print("3. List All Books")
            print("4. Remove Book")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.find_book()
            elif choice == "3":
                self.list_all_books()
            elif choice == "4":
                self.remove_book()
            elif choice == "5":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    book_manager = BookManager()
    book_manager.main_menu()
