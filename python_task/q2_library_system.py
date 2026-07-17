# Dictionary to store books
catalog = {}

# List to store borrowed book IDs
borrowed_books = []

# Set to store unique member IDs
members = set()


# Function to add a book
def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)


# Function to borrow a book
def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog:
        if book_id not in borrowed_books:
            borrowed_books.append(book_id)
            print(f"Book ID {book_id} borrowed successfully.")
        else:
            print(f"Book ID {book_id} is already borrowed.")
    else:
        print("Book does not exist in the library.")


# Function to return a book
def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book ID {book_id} returned successfully.")
    else:
        print("Book was not borrowed.")


# Function to register a member
def register_member(members, member_id):
    members.add(member_id)      # Set automatically ignores duplicates


# Function to show available books
def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"Book ID: {book_id}")
            print(f"Title   : {title}")
            print(f"Author  : {author}")
            print(f"Year    : {year}")
            print()


# Main Function
def main():

    # Add 4 books
    add_book(catalog, 101, "Python Basics", "John Smith", 2020)
    add_book(catalog, 102, "Data Structures", "Alice Brown", 2021)
    add_book(catalog, 103, "Machine Learning", "David Lee", 2022)
    add_book(catalog, 104, "Artificial Intelligence", "James Wilson", 2023)

    # Register members
    register_member(members, 1)
    register_member(members, 2)
    register_member(members, 3)
    register_member(members, 2)      # Duplicate (ignored)

    print("Registered Members:", members)

    # Borrow two books
    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 103)

    # Return one book
    return_book(borrowed_books, 101)

    # Display available books
    show_available(catalog, borrowed_books)


# Run the program
main()