def multiplication (number):
     counter= 1
     while(counter<9):
      operation = number * counter
      counter+=1
      print(operation)

user_input=int(input("Insert Decimal"))
multiplication(user_input)