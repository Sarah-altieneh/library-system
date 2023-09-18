from datetime import datetime

# Define a class to represent a book
class Book:
    def __init__(self, title, author, price, copies=1):
        self.title = title
        self.author = author
        self.price = price
        self.available = copies  # Number of available copies
        self.due_date = None

    # Method to borrow a book
    def borrow(self, due_date):
        if self.available > 0:
            self.available -= 1  # Decrease the available copies
            self.due_date = due_date
            return True
        else:
            return False

    # Method to return a book
    def return_book(self, return_date):
        if self.due_date:
            try:
                return_date = datetime.strptime(return_date, "%Y-%m-%d")  # Convert return_date to datetime
                self.available += 1  # Increase the available copies when the book is returned
                days_late = (return_date - datetime.strptime(self.due_date, "%Y-%m-%d")).days  # Calculate days late
                if days_late > 0:
                    fine = days_late * 2  # Charge $2 per day for late return
                    return fine
            except ValueError:
                return "Invalid date format. Please use yyyy-mm-dd."
        self.due_date = None
        return 0  # No fine if returned on time or book was not borrowed

# Define a class to represent a library
class Library:
    def __init__(self):
        self.sections = {}  # Dictionary to store library sections and their books
        self.users = {}  # Dictionary to store users and their borrowed books
        self.staff_credentials = {"staff1": "password1", "staff2": "password2"}  # Staff credentials

    # Method to add a new section to the library
    def add_section(self, section_name):
        if section_name not in self.sections:
            self.sections[section_name] = []  # Create a new section if it doesn't exist
            print(f"Section '{section_name}' added to the library.")
        else:
            print(f"Section '{section_name}' already exists in the library.")

    # Method to add a new book to a section
    def add_book(self, section_name, title, author, price, copies=1):
        if section_name in self.sections:
            book = Book(title, author, price, copies)
            self.sections[section_name].append(book)  # Add the book to the specified section
            print(f"Book '{title}' by {author} added to section '{section_name}' with {copies} copies.")

    # Method to remove a book from a section
    def remove_book(self, section_name, title, author):
        if section_name in self.sections:
            for book in self.sections[section_name]:
                if book.title == title and book.author == author:
                    self.sections[section_name].remove(book)  # Remove the book from the section
                    print(f"Book '{title}' by {author} removed from section '{section_name}'.")
                    return
            print(f"Book '{title}' by {author} not found in section '{section_name}'.")
        else:
            print(f"Section '{section_name}' not found in the library.")

    # Method to set the price of a book
    def set_book_price(self, section_name, title, author, price):
        if section_name in self.sections:
            for book in self.sections[section_name]:
                if book.title == title and book.author == author:
                    book.price = price  # Update the price of the book
                    print(f"The price of '{book.title}' by {book.author} in section '{section_name}' has been updated to ${price}.")
                    return
            print(f"Book '{title}' by {author} not found in section '{section_name}'.")
        else:
            print(f"Section '{section_name}' not found in the library.")

    # Method to borrow a book from the library
    def borrow_book(self, section_name, title, author, user, due_date):
        if section_name in self.sections:
            for book in self.sections[section_name]:
                if book.title == title and book.author == author:
                    if book.borrow(due_date):
                        user.borrowed_books.append(book)  # Add the borrowed book to the user's list
                        print(f"User '{user.name}' borrowed '{book.title}' from section '{section_name}' until {due_date}.")
                    else:
                        print(f"Book '{book.title}' is not available for borrowing.")
                    return
            print(f"Book '{title}' by {author} not found in section '{section_name}'.")
        else:
            print(f"Section '{section_name}' not found in the library.")

    # Method to return a borrowed book to the library
    def return_book(self, section_name, title, author, user, return_date):
        if section_name in self.sections:
            for book in self.sections[section_name]:
                if book.title == title and book.author == author:
                    fine = book.return_book(return_date)
                    if fine > 0:
                        print(f"User '{user.name}' returned '{book.title}' to section '{section_name}' late. Fine: ${fine}")
                    else:
                        print(f"User '{user.name}' returned '{book.title}' to section '{section_name}' on time.")
                    user.borrowed_books.remove(book)  # Remove the returned book from the user's list
                    return
            print(f"Book '{title}' by {author} not found in section '{section_name}'.")
        else:
            print(f"Section '{section_name}' not found in the library.")

    # Method to display all sections and books for regular users
    def display_sections_and_books(self):
        if self.sections:
            print("Sections in the library:")
            for section_name in self.sections:
                print(section_name)
                if self.sections[section_name]:
                    print("Books in this section:")
                    for book in self.sections[section_name]:
                        print(f"Title: {book.title}, Author: {book.author}, Price: ${book.price}")
                else:
                    print("No books in this section.")
                print("-" * 30)
        else:
            print("There are no sections in the library.")

    # Method to list all sections
    def list_sections(self):
        print("Sections in the library:")
        for section_name in self.sections:
            print(section_name)

    # Method to list books in a section
    def list_books_in_section(self, section_name):
        if section_name in self.sections:
            print(f"Books in section '{section_name}':")
            for book in self.sections[section_name]:
                print(f"Title: {book.title}, Author: {book.author}, Price: ${book.price}, Copies available: {book.available}")
        else:
            print(f"Section '{section_name}' not found in the library.")

    # Method to count the number of each book in a section
    def count_books_in_section(self, section_name):
        if section_name in self.sections:
            book_counts = {}  # Dictionary to store book counts
            for book in self.sections[section_name]:
                title = book.title
                if title in book_counts:
                    book_counts[title] += book.available  # Increment the count by available copies
                else:
                    book_counts[title] = book.available  # Initialize the count to available copies
            print(f"Number of books in section '{section_name}':")
            for title, count in book_counts.items():
                print(f"Title: {title}, Count: {count}")
        else:
            print(f"Section '{section_name}' not found in the library.")

    # Method to allow a user to buy a book
    def buy_book(self, section_name, title, author, user_name):
        if section_name in self.sections:
            user = self.users.get(user_name)
            if user is None:
                user = User(user_name)
                self.users[user_name] = user
            purchased_books = []  # List to keep track of purchased books
            total_price = 0  # Initialize the total price
            for book in self.sections[section_name]:
                if book.title == title and book.author == author and book.available > 0:
                    purchased_books.append(book)  # Add the book to the purchased list
                    total_price += book.price  # Add the book price to the total
                    book.borrow(None)  # Decrease available copies
            if purchased_books:
                print(f"User '{user_name}' successfully purchased the following books from section '{section_name}':")
                for book in purchased_books:
                    print(f"Title: {book.title}, Author: {book.author}, Price: ${book.price}")
                print(f"Total Price: ${total_price}")
            else:
                print(f"No available books matching the specified criteria found in section '{section_name}'.")
        else:
            print(f"Section '{section_name}' not found in the library.")

    # Method to register a new staff member
    def register_staff(self):
        staff_name = input("Enter staff name: ")
        passcheck=True
        while passcheck:
            try:
                staff_password = input("Enter staff password: ")
                if len(staff_password) >=8:
                    passcheck=False
                else :
                    continue    
            except ValueError:
                print ('The password must be at least 8 characters long')

        self.staff_credentials[staff_name] = staff_password  # Add the staff member to the credentials dictionary
        print(f"Staff member '{staff_name}' registered successfully.")

# Define a class to represent a user
class User:
    def __init__(self, name, password):
        self.name = name
        if len(password) >= 8:
            self.password = password
        else:
            raise ValueError("Password must be at least 8 characters long.")
        self.borrowed_books = []  # List to store books borrowed by the user

# Create an instance of the Library class
this_library = Library()

# Main program loop
while True:
    print("\nLibrary Management System")
    user_type = input("Are you a staff member (yes/no)? ").strip().lower()

    if user_type == 'yes':
        new_staff = input("Are you a new staff member (yes/no)? ").strip().lower()
        if new_staff == 'yes':
            this_library.register_staff()
            continue  # Go back to the beginning of the loop
        # Staff authentication
        staff_username = input("Enter staff username: ")
        passcheck=True
        while passcheck:
            try:
                staff_password = input("Enter staff password: ")
                if len(staff_password) >=8:
                    passcheck=False
                else :
                    continue    
            except ValueError:
                print ('The password must be at least 8')
        else:
            if staff_username in this_library.staff_credentials and this_library.staff_credentials[staff_username] == staff_password:
                print("Staff Member Options:")
                print("1. Add Section")
                print("2. Add Book to Section")
                print("3. Remove Book from Section")
                print("4. Set Book Price")
                print("5. List Sections")
                print("6. List Books in Section")
                print("7. Number of each book")
                print("8. Quit")
            else:
                print("Invalid staff credentials. Access denied.")
                continue
    else:
        print("Regular User Options:")
        print("1. List Sections")
        print("2. List Books in Section")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Buy Book")
        print("6. Quit")
    choice = input("Enter your choice: ")
    print("\n")
    if user_type == 'yes':
        if choice == '1':
            section_name = input("Enter the section name: ")
            this_library.add_section(section_name)

        elif choice == '2':
            this_library.list_sections()
            section_name = input("Enter the section name from the showen: ")
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            pricecheck=True
            while pricecheck:
                try:
                   price = float(input("Enter the book's price: "))
                   pricecheck=False
                except ValueError:
                    print('you entered a wrong value')   
            copiescheck=True
            while copiescheck:
                try:
                   copies = int(input("Enter the number of copies: "))
                   copiescheck=False
                except ValueError:
                    print('you entered a wrong value')
            this_library.add_book(section_name, title, author, price, copies)

        elif choice == '3':
           
            section_name = input("Enter the section name: ")
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            due_date = input("Enter the due date (yyyy-mm-dd): ")
            user_name = input("Enter your name: ")
            user = this_library.users.get(user_name)
            if user is None:
                user = User(user_name)
                this_library.users[user_name] = user
            this_library.borrow_book(section_name, title, author, user, due_date)

        elif choice == '4':
           
            section_name = input("Enter the section name: ")
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            return_date = input("Enter the return date (yyyy-mm-dd): ")
            user_name = input("Enter your name: ")
            user = this_library.users.get(user_name)
            if user is not None:
                this_library.return_book(section_name, title, author, user, return_date)
            else:
                print(f"User '{user_name}' not found.")

        elif choice == '5':
            this_library.list_sections()

        elif choice == '6':
            section_name = input("Enter the section name: ")
            this_library.list_books_in_section(section_name)

        elif choice == '7':
            section_name = input("Enter the section name: ")
            this_library.count_books_in_section(section_name)

        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
    else:
        if choice == '1':
            this_library.list_sections()

        elif choice == '2':
            section_name = input("Enter the section name: ")
            this_library.list_books_in_section(section_name)

        elif choice == '3':
            this_library.display_sections_and_books()  # Display sections and books for regular users
            user_name = input("Enter your name: ")
            section_name = input("Enter the section name: ")
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            due_date = input("Enter the due date (yyyy-mm-dd): ")
            user = this_library.users.get(user_name)
            if user is None:
                user = User(user_name)
                this_library.users[user_name] = user

               
            this_library.borrow_book(section_name, title, author, user, due_date)

        elif choice == '4':
            this_library.display_sections_and_books()  # Display sections and books for regular users
            user_name = input("Enter your name: ")
            section_name = input("Enter the section name: ")
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            return_date = input("Enter the return date (yyyy-mm-dd): ")
            user = this_library.users.get(user_name)
            if user is not None:
                this_library.return_book(section_name, title, author, user, return_date)
            else:
                print(f"User '{user_name}' not found.")

        elif choice == '5':
            this_library.display_sections_and_books()  # Display sections and books for regular users
            user_name = input("Enter your name: ")
            section_name = input("Enter the section name: ")
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            this_library.buy_book(section_name, title, author, user_name)

        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
