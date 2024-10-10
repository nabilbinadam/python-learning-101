"""

Create a Book class with the following attributes:
title
author
isbn
prices (a list to store different prices of the book)
Implement the following methods:
__init__: Initializes the book with title, author, and ISBN number.
info: Prints the book's title, author, and ISBN.
doPayment: Calculates and returns the total price of all prices in the prices list.
Create several book objects with different titles, authors, and ISBN numbers.
Set the prices for one or more book objects and print the total amount to be paid.
Optionally, print the information for each book created.

"""

class Book:

    def __init__(self,tittle,author,ISBN,payment) -> None: # create?


        print("successfuly created!")
        self.tittle= tittle
        self.author= author
        self.ISBN=ISBN
        self.Payment= payment
        self.prices= []
        

        
        


    def doPayment(self):  # any list we need to do for loop 

        total=0
        for i in self.prices :
           print(i)
           total += i

        return total     
           
           
     
        
        
    

     
    def info (self):  # read
        print("Tittle:",self.tittle)
        print("ISBN:",self.ISBN)
        print("Author:",self.author)
        print("Payment:",self.Payment)
        print("Prices:",self.prices)

        

    
    
    
    def delete(self,info):
        #show info 
        self.tittle.info()
        input = str(input("Choose Book To Delete:"))

        if input in self.tittle:
            input.split()
        


    
     def read (tittle,ISBN,Author,Payment):
        pass 



book1 = Book("Das Kapital","123123","Karl Marx","Cash")
book2 = Book("Phenomology of Spirit","12356","Hegel","Cash")
book1.prices= [123,123,123,123]
book2.prices= [123,143,134,533]
book2.info()
print("----------")
book1.info()

print(book2.doPayment())

book1.delete()

