print("Welcome to the Book Title Library!")
print()

#Prompt the user about options avaiable
print("Choose an option: \n 1.Add a book \n 2.Remove a book \n 3.View all books \n 4.Exit")
print()
# list of books in library
books_available = []
#using while loop to ensure program run continuous
while True:
    user_input = input("Please enter your choice : ")

    #I noticed int(input) requires user to enter a number, to prevent error, I'm making input a string
    #allow user add books to list
    if user_input == "1":
        add_books = input("Enter the books you would like to add: ").title()

        add_books = add_books.split(",")
        books_available.extend(add_books)

        print(f"Here are the list of books available: {books_available}")

    #remove books from list
    elif user_input == "2":
        remove_books = input("Enter the book you would like to remove: ").title()

        while remove_books in books_available:
            if remove_books in books_available :
                books_available.remove(remove_books)
                print(f"{remove_books} have been removed from the list")
            else :
                print("Book is not in list")
            remove_books = input("Enter the book you would like to remove , or Press any q to return: ").strip().title()
            if remove_books == "Q":
             #adding continue to skip and stop the remove loop   
                continue
        print(f"Here is the updated list of books: {books_available}")

    #View all books in list
    elif user_input == "3":
        print(f"Here is a list of all the books available: {books_available}")
    #quit the program
    elif user_input == "4":
        print("Goodbye!")
        #add break to end the program
        break
    else:
        print("You entered an invalid choice,\nEnter 1 to add a book, Enter 2 to remove a book, Enter 3 to view books, Enter 4 to quit")

