# Project 1 :- Library Mangement System 
class Library :
    def __init__(self,listOfBooks ):
        self.books = listOfBooks

    def display (self):   # Display the books name
        for books in self.books:
            print("\t- " + books)
    
    def borrowBooks (self , bookName):
        if bookName in self.books:
            print("You has been issued {self.bookName} .")
            # If user borrow one book then the book should br removed
            self.books.remove(bookName)
            
        else:
            print("Sorry! This book is already issued by someone else . Please wait until the book is returned")
            
            
    def returnBook(self , bookName):
        self.books.append(bookName)
        print("Thanks for returing this book.")

    #  Class library functions are completed.


class Student:
    # function for borrowing the book
    def requestBook (self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book
        #  function for returing the book
    def returnBook (self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
       
# Maintaing the library:
if __name__ == "__main__":
    l = Library(["Learn Pyhton" , "Algorithms" , "Django" , "C Lanuage" , "Machine Leraning"])
    student = Student()
    # Menu:
    while True:
        welcomeMsg = '''===== ** Welcome to the G/Library ** =====
        Please choose an option :
        - Press 1 for listall the books
        - Press 2 for Borrow the books
        - Press 3 for Return a book
        - Press 4 Exit the library
        '''
        print(welcomeMsg) 
        a = input("Enter a Choise: ")
       
        if a == '1':
            l.display()
        elif a =='2':
            l.borrowBooks(student.requestBook())
        elif a == '3':
            l.returnBook(student.returnBook())
        elif a == '4' :
            print("Thanks for choosing G/Library.")
            exit()
        else:
            print("Invalid choice!")
        
        
        
            

       

