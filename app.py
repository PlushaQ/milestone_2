import json
books = []


def load_data():  # Function that loads json database file
    with open("utils/database.txt") as database:
        if database is not None:
            global books
            books = json.load(database)
        else:
            pass


def book_detail_input():  # This function gathers user's data about a book
    title = input("Enter the book title: ").title()
    author = input("Enter the book author: ").title()
    is_it_read = is_this_book_read_already()
    if is_it_read is True:
        date_of_read = date_of_read_function()
        rating = rating_function()
    else:
        date_of_read = "Not read yet"
        rating = "Not read yet"

    book = {'title': title,
            'author': author,
            'read': is_it_read,
            'date_of_read': date_of_read,
            'rating': rating}
    return book


def is_this_book_read_already():  # This function ask user about book read status
    book_read_status = None
    while book_read_status is None:
        is_it_read_input = input("Have you read this book already? \nyes/no? ").lower()
        if is_it_read_input == 'yes':
            book_read_status = True
            break
        elif is_it_read_input == 'no':
            book_read_status = False
            break
        else:
            print("Unknown command! Please try again. ")
    return book_read_status


def date_of_read_function():  # This function ask user about date of finishing book
    date_of_read = input("When did you finish this book? DD/MM/YYYY ")
    return date_of_read


def rating_function():  # This function ask user about his personal rating about book
    rating = 0
    while rating not in range(1, 11):
        try:
            rating = int(input("How do you rate this book in scale from 1 to 10? "))
        except ValueError:
            print("You entered wrong value. Please try again.")
    return rating


def book_add_to_list():  # this function adds book to list
    book_entry = book_detail_input()
    books.append(book_entry)


def show_books():  # this function prints books list
    for book in books:
        print(f'''{book["title"]} by ({book["author"]}).
        Read? {book["read"]}.
        When read? {book["date_of_read"]}
        Rating: {book["rating"]} \n''')


def finding_books():  # function for finding books by title or author
    author_or_title = input("Do you want to search by title or by author? title/author: ").lower()
    if author_or_title == "title":
        book_title = input("What book do you search for? ").title()
        for book in books:
            if book["title"] == book_title:
                print(f'''{book["title"]} by ({book["author"]}). 
                Read? {book["read"]}.
                When read? {book["date_of_read"]}
                Rating: {book["rating"]} \n''')
            else:
                print('Your book is not on the list')

    elif author_or_title == "author":
        book_author = input("What author do you search for? ").title()
        for book in books:
            if book["author"] == book_author:
                print(f'''{book["title"]} by ({book["author"]}). 
                Read? {book["read"]}.
                When read? {book["read"]}
                Rating: {book["rating"]} \n''')
            else:
                print("Your author is not on the list")
    else:
        print("You entered wrong command. Please try again. ")


def book_read_status_change():  # This function changes read book status from False to True or vice versa
    book_title = input("Please enter a title of book you want to change read status: ").title()
    for book in books:
        if book['title'] == book_title and book["read"] is False:
            book['read'] = True
            book['date_of_read'] = date_of_read_function()
            book['rating'] = rating_function()
        elif book['title'] == book_title and book["read"] is True:
            user_choice = input("You already finished this book. Do you want to change it to unread? yes/no ")
            while user_choice != "no":
                if user_choice == "yes":
                    book['read'] = False
                    book['rating'] = "Not read yet"
                    book['date_of_read'] = "Not read yet"
                    print(f"{book['title']} status is {book['read']}")
                    break
                else:
                    print("You entered wrong command!")
                    user_choice = input("You already finished this book. Do you want to change it to unread? yes/no ")


def book_read_date_change():  # This function changes date of read
    book_title = input("Please enter a title of book you want to change date of read: ").title()
    for book in books:
        if book['title'] == book_title:
            if book['read'] is True:
                book['date_of_read'] = date_of_read_function()
            else:
                print("You didn't read this book")


def book_rating_change():  # This function changes rating
    book_title = input("Please enter a title of book you want to change rating: ").title()
    for book in books:
        if book['title'] == book_title:
            book['rating'] = rating_function()


def delete_book():  # This function deletes book from database
    global books
    name = input("What book you want to remove from your list? ").title()
    books = [book for book in books if book["title"] != name]


def save_to_file():  # This function saves data in file
    with open("utils/database.txt", "w") as file:
        json.dump(books, file)
    print("Your data is saved now. \n")


def save_to_file_and_quit():  # This function saves data in file and quit the app
    with open("utils/database.txt", "w") as file:
        json.dump(books, file)
    print("Your data is saved now. \n")
    print("Goodbye, have a good day!")


MENU_PROMPT = """Please choose what do you want to do:
- 'a' to add new book
- 'l' to list all books
- 'f' to find book by author or title
- 'r' to change book read status
- 't' to change date of read of a book
- 'o' to change rating of a book
- 'd' to delete a book
- 's' to save changes
- 'q' to save changes and quit
Your choice: """

user_options = {
    "a": book_add_to_list,
    "l": show_books,
    "f": finding_books,
    "r": book_read_status_change,
    "t": book_read_date_change,
    "o": book_rating_change,
    "d": delete_book,
    "s": save_to_file,
    "q": save_to_file_and_quit,
}


def menu():
    selection = input(MENU_PROMPT).lower()
    if selection == 'q':
        save_to_file_and_quit()
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


load_data()
menu()
