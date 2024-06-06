# ChatGPT link: https://chatgpt.com/c/acf1b5a8-1db2-42f2-b1c7-cb883c3500f1

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
    
    def __str__(self):
        return f"'{self.title}'"
    
    def __repr__(self):
        return f"Author: {self.author}, Copies available: {self.copies}"
    
    def lend_copy(self): # reduce the number of copies by 1, if there are any copies available.
        if self.copies > 0:
            self.copies -= 1
            print(f"1 copy of {self.title} on loan. {self.copies} copies remaining.")
        else:
            print(f"No copies of {self.title} available.")

    def return_copy(self): # increase the number of copies by 1
        self.copies += 1
        print(f"1 copy of {self.title} returned. {self.copies} copies on hand.")

class Library:
    def __init__(self):
        self.books = {}
    
    def __repr__(self):
        library_books = ', '.join([f"'{title}' by {book.author}, {book.copies} copies" for title, book in self.books.items()]) # using .items() returns k, v pairs
        return f"Books in library: [{library_books}]"

    def add_book(self, title, author, copies): # adds a new book to the library. if book already exists it should increase the number of copies.
        if title in self.books:
            self.books[title].copies += copies
            print(f"{title} found in library. Total copies of increased by {copies}.")
        else:
            self.books[title] = Book(title, author, copies)
            print(f"New book added to library: '{title}' by {author}, {copies} copies.")

    def lend_book(self, title): # lends out a book if it's available
        if title in self.books:
            if self.books[title].copies >= 1:
                self.books[title].copies -= 1
                print(f"1 copy of {self.books[title]} on loan. {self.books[title].copies} copies remaining.")
            else:
                print(f"No copies of {self.books[title]} available.")
        else:
            print("Book not found.")

    def return_book(self, title): # returns a book to the library
        if title in self.books:
            self.books[title].copies += 1
            print(f"1 copy of {self.books[title]} returned. {self.books[title].copies} copies available.")
        else:
            print("Book not found.")

    def display_books(self): # displays all the books in the library along with author and copies available
        for title, book in self.books.items():
            print(f"'{title}' by {book.author}, {book.copies} copies available.")
    
    def print_structure(self):
        print(self.books)

# Create a library
library = Library()

# Add books to the library
library.add_book("1984", "George Orwell", 4)
library.add_book("To Kill A Mockingbird", "Harper Lee", 2)

# Lend out a book
library.lend_book("1984")

# Return a book
library.return_book("1984")

# Display all books
library.display_books()

# Print the structure of the dictionary
library.print_structure()