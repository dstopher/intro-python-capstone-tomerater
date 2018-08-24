# USER section
# define what a user is
class User:
    # constructor for a user object; relies on a name and email address
    def __init__(self, name, email):
        self.name = name
        # try to confirm validity of email address input
        if self.confirm_valid_email(email):
            self.email = email
        else:
            self.email = ""
            print("email address invalid!")
        self.books = {}
    # method to return email address
    def get_email(self):
        return self.email
    # method to update email address
    def change_email(self, new_email):
        self.email = new_email
        print("Email address updated.")
    # string representation of user object; describes user in terms of name, email address, and books read
    def __repr__(self):
        return (str(self.name) + ", email: " + str(self.email) + ", books read: " + str(len(self.books)))
    # method for checking user equivalence; requires name and email address to be equivalent
    def __eq__(self, other_user):
        if (self.name == other_user.name) and (self.email == other_user.email):
            result = True
        else:
            result = False
        return result
    # method for adding a user's rating of a book that he/she has read    
    def read_book(self, book, rating = None):
        self.books[book] = rating
    # method for getting the user's average of all ratings
    def get_average_rating(self):
        total = 0
        average_rating = 0.0
        ratings_counter = 0
        for book in self.books:
            if self.books[book] is not None:
                ratings_counter += 1
                total += self.books[book]
        average_rating = total / ratings_counter
        return average_rating
    # method for verifying user's email address has key elements (@, .com/.edu/.org)
    def confirm_valid_email(self, email):
        if "@" in email and ((email[-4:] == ".com") or (email[-4:] == ".edu") or (email[-4:] == ".org")):
            result = True
        else:
            result = False
        return result
            
# BOOK section        
# define what a book is        
class Book:
    # constructor for a book object; relies on a title (a string) and ISBN identifier (a number)
    def __init__(self, title, isbn):
        self.title = str(title)
        self.isbn = int(isbn)
        self.ratings = []
    # method to return book's title
    def get_title(self):
        return self.title
    # method to return book's ISBN identifier
    def get_isbn(self):
        return self.isbn
    # method to update book's ISBN identifier
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("ISBN updated.")
    # method to add a rating (in range [0,4]) of book
    def add_rating(self, rating):
        if (rating == None):
            pass
        elif (rating >= 0) and (rating <= 4):
            self.ratings.append(rating)
        else:
            print("Invalid Rating")
    # method for checking book equivalence; requires title and ISBN to be equivalent
    def __eq__(self, other_book):
        if (self.title == other_book.title) and (self.isbn == other_book.isbn):
            result = True
        else:
            result = False
        return result
    # method for getting the average rating for this book
    def get_average_rating(self):
        total = 0
        average_rating = 0.0
        number_ratings = len(self.ratings)
        for rating in self.ratings:
            total += rating
        average_rating = total / number_ratings
        return average_rating
    # method for making Book hashable
    def __hash__(self):
        return hash((self.title, self.isbn))
        
        
# define subclass for fiction books        
class Fiction(Book):
    # constructor for a fiction book
    def __init__(self, title, author, isbn):
        Book.__init__(self, title, isbn)
        self.author = author
    # method to get book's author
    def get_author(self):
        return self.author
    # string representation of fiction book object; describes book in terms of title and author
    def __repr__(self):
        return (str(self.title) + " by " + str(self.author))

# define subclass for nonfiction books        
class Non_Fiction(Book):
    # constructor for a nonfiction book
    def __init__(self, title, subject, level, isbn):
        Book.__init__(self, title, isbn)
        self.subject = str(subject)
        self.level = str(level)
    # method to get book's subject
    def get_subject(self):
        return self.subject
    # method to get book's level
    def get_level(self):
        return self.level        
    # string representation of nonfiction book object; describes book in terms of title, level, and subject
    def __repr__(self):
        return (str(self.title) + ", a " + str(self.level) + " manual on " + str(self.subject))
        
# TOMERATER (interaction between USERs and BOOKs) section
# define tomerater class
class TomeRater:
    # constructor for a user object; relies on a name and email address
    def __init__(self):
        self.users = {}
        self.books = {}
    # method to instantiate a Book object based on title and ISBN
    def create_book(self, title, isbn):
        return Book(title, isbn)
    # method to instantiate a Fiction object (subclass of Book) based on title, author ISBN
    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)
    # method to instantiate a NonFiction object (subclass of Book) based on title, subject, level, ISBN
    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)
    # method to indicate that a user has read a new book
    def add_book_to_user(self, book, email, rating = None):
        # check to ensure user exists
        if email in self.users:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email " + str(email) + "!")
    # method to create a new user
    def add_user(self, name, email, user_books = None):
        # check to ensure user does not already exist
        if email in self.users:
            print("This user already exists! Cannot be added.")
        else:
            self.users[email] = User(name, email)
            if user_books is not None:
                for book in user_books:
                   self.add_book_to_user(book, email)
    # method to print all book objects
    def print_catalog(self):
        for i in self.books:
            print(i)
    # method to print all user objects
    def print_users(self):
        for i in self.users:
            print(i)
    # method to determine the most-read book
    def get_most_read_book(self):
        max_read_value = 0
        for i in self.books:
            if self.books[i] > max_read_value:
                max_read_value = self.books[i]
                most_read = i
        return most_read
    # method to determine the book with highest average rating
    def highest_rated_book(self):
        max_rating = 0
        highest_rated = ""
        for i in self.books:
            rating = i.get_average_rating()
            if rating > max_rating:
                max_rating = rating
                highest_rated = i
        return highest_rated
    # method to return the user who has rated books the highest
    def most_positive_user(self):
        max_rating = 0
        for user in self.users:
            rating = self.users[user].get_average_rating()
            if rating > max_rating:
                max_rating = rating
                most_positive = user
        return most_positive
    # method to check that all books have unique ISBN identifiers
    def check_ISBN_uniqueness(self):
        # empty list to be populated with pairs of Book objects that have same ISBN
        duplicate_ISBN_books = []
        # iterate through dictionary of book objects
        for i in self.books:
            # iterate through dictionary of book objects again to have comparison list
            for j in self.books:
                # disregard cases where ISBN identifiers do not match (expected behavior)    
                if i.isbn != j.isbn:
                    pass
                # disregard the case where ISBN in list i is equivalent to ISBN in list j because the book is the same
                elif i.__eq__(j):
                    pass
                # add to empty duplicate list the cases where two ISBNs are equivalent but the two books are not, but only if the pair is not already listed (from previous iteration through list)
                else:
                    if [j,i] in duplicate_ISBN_books:
                        pass
                    else:
                        duplicate_ISBN_books.append([i,j])
        # report out if there are duplicates, based on length of duplicate list                
        if len(duplicate_ISBN_books) == 0:
            result = "No ISBN duplicates"
        else:
            result = "There are duplicate ISBNs!: " + str(duplicate_ISBN_books)
        return result
    # method to describe general contents of a TomeRater object
    def __repr__(self):
        return ("The users in this database are:\n" + str(self.users) + ".\n\n" + "The books in this database, and the number of people who have read each, are:\n" + str(self.books))        