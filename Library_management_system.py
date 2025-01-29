from abc import ABC,abstractmethod

class Library(ABC):

    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.books= []    

    @abstractmethod
    def borrow_book(self,book_name):
        pass
    
    @abstractmethod
    def return_book(self,book_name):
        pass

    def details(self):
        print("-"*100)
        print( f"""
               Member name  : {self.name}
               Member Type  : {type(self).__name__}
               Member id    : {self.id}
               Books issued : {self.books}                           
                """)
        print("-"*100)



class Student(Library):

    max_Books = 3  

    def borrow_book(self,book_name,id):
        if (id==self.id):
            if (len(self.books)<Student.max_Books):
                self.books.append(book_name)     
            else:
                print("-"*100)
                print( f"You cannot borrow more than {Student.max_Books} books." )  
                print("-"*100)
        else:
            print("-"*100)
            print("Invalid ID")
            print("-"*100)
       

    def return_book(self,book_name,id):
        if(id == self.id):
            if (book_name in self.books):
                self.books.remove(book_name)
                print("-"*100)
                print( f"Thanks for returning book. Now you can issue {Student.max_Books-len(self.books)} more books.")
                print("-"*100)
            else:
                print("-"*100)
                print(f" This is not the book you borrowed. These are the books you borrowed : {self.books}")
                print("-"*100)
        else:
            print("-"*100)
            print("Invalid ID")
            print("-"*100)
        


class Teacher(Library):
    max_Books = 5

    def borrow_book(self,book_name,id):
        if(id == self.id):
            if (len(self.books)<Teacher.max_Books):
                self.books.append(book_name)     
            else:
                print("-"*100)
                print(f"You cannot borrow more than {Teacher.max_Books} books")
                print("-"*100)
        else:
            print("-"*100)
            print("Invalid ID")
            print("-"*100)
        
        
    def return_book(self,book_name,id):
        if (id == self.id):
            if (book_name in self.books):
                self.books.remove(book_name)
                print("-"*100)
                print(f"Thanks for returning book. Now you can issue {Teacher.max_Books-len(self.books)} more books.")
                print("-"*100)
            else:
                print("-"*100)
                print(f"This is not the book you borrowed. These are the books you borrowed : {self.books}")
                print("-"*100)
        else:
            print("-"*100)
            print("Invalid ID")
            print("-"*100)
        


s1 = Student("Sarthak",9000)
s1.borrow_book("Maths",9000)
s1.borrow_book("Biology",9000)
s1.borrow_book("Law_of_attraction",9000)
s1.details()
s1.borrow_book("Good_Habits",9000)
s1.return_book("Biology",9000)
s1.details()


t1 =Teacher("Manish",1080)
t1.borrow_book("Python",1080)
t1.borrow_book("CPP",1080)
t1.details()
t1.borrow_book("JAVA",1080)
t1.borrow_book("RUBI",1080)
t1.return_book("Python",1080)
t1.details()







