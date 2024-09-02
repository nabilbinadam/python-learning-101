"""
Create a function that checks 
if a given string is a 
palindrome (reads the same forwards and backwards).
"""

string_input= str(input("insert string:"))
object1=[]
object2=[]

def palindrome(reversed):             
        if string_input == reversed :
            print("its is a palindrome")

        else:
           print("not a palindrome")
     


def reversed (string_input):
      for strings in range(len(str(string_input))):
            converted = list(reversed(strings))
            print(converted)
            return converted
      
reversed(string_input)
palindrome(reversed())      