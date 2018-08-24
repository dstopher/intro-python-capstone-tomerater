from TomeRater import *

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
#Original line in file
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
#Test line for same ISBN, different book
#nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 1929452)


novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")
#Test line to ensure user with same email address is not added twice
#Tome_Rater.add_user("Alan Turing2", "alan@turing.com")
#Test line for invalid email address
#Tome_Rater.add_user("Alan Turing", "alan@turing")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.get_most_read_book())

# other test functions for attributes/methods
def print_usernames():
    for i in Tome_Rater.users:
        print(Tome_Rater.users[i].name)
    return

def print_useremails():
    for i in Tome_Rater.users:
        print(Tome_Rater.users[i].email)
    return

def print_userbooks():
    for i in Tome_Rater.users:
        print(Tome_Rater.users[i].books)
    return

def print_useremails_method():
    for i in Tome_Rater.users:
        print(Tome_Rater.users[i].get_email())
    return

def print_userrepr():
    for i in Tome_Rater.users:
        print(Tome_Rater.users[i].__repr__())
    return

def print_userequivalence():
    for i in Tome_Rater.users:
        for j in Tome_Rater.users:
            print(i)
            print(j)
            print(Tome_Rater.users[i].__eq__(Tome_Rater.users[j]))
    return
    
def print_booktitles():
    for i in Tome_Rater.books:
        print(i.title)
    return

def print_bookisbn():
    for i in Tome_Rater.books:
        print(i.isbn)
    return

def print_bookratings():
    for i in Tome_Rater.books:
        print(i.ratings)
    return

def print_bookequivalence():
    for i in Tome_Rater.books:
        for j in Tome_Rater.books:
            print(i)
            print(j)
            print(i.__eq__(j))
    return