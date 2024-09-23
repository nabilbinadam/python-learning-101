"""
Duplicate User

Tina works in a consultancy, and she was currently associated with the task 
where she had to remove the duplicate users from the list by comparing the phone 
numbers of the users. She thought writing code as per the
 requirement would make her work easier. So she asks one of her friends, 
 to write a code for her. Imagine you are Tina's friend, 
 help her by writing the code as it is required. 

Write a Python code to check duplicate user details.
 There can be only one user with a specific mobile number. 
 If two users exist with the same mobile number they are duplicate. 
 Check whether user information is the same or not by overriding the equals method.

Create a User class with the following attributes 

Attributes

Datatype

name

str

username

str

password

str

mobile_number

int

 

Use __init__() constructor to initialize the variables with respect to class.

Override __eq__() method that compares mobile_number of the two objects.

 

Input format :

Input consists of 2 user’s details, 
which contains (name, username, password, mobile_number).

Output format :

The output is a string value, denoting whether the
 users were same or not by comparing the mobile number of the user.

 

[All Texts in bold corresponds to the input and rest are output] 

Sample Input and Output - 1:
Enter the details of User 1
Name :
Meena
Username :
Meena2020
Password :
Basic
Mobile Number :
1234567890
Enter the details of User 2
Name :
Meena
Username :
Meena1010
Password :
Probob
Mobile Number :
0987654321
User 1 and User 2 are not equal









"""

class User :
    def __init__(self,name,username,password,mobile_number) :

        self.name= name
        self.username= username
        self.password = password
        self.mobile_number =mobile_number

     


        
user1=User('Nabil','asdasd','1235',123123)
print(user1.name)
print(user1.password)
print(user1.username)
print(user1.mobile_number)