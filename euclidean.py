#take 2 int input 
#output = compute GCD using Euclidiean algo

input_one = int(input("Insert Input one :"))
input_two = int(input("Insert Input two :"))

counter = 0 
sum= input_one + input_two 
remainderZero= False
replace=0
while(replace!=0):
  if(input_one>input_two):
    remainder = input_one%input_two
    replace = remainder % input_two
    remainderZero= True

    print(replace)
  elif(input_one<input_two):
    remainder2 = input_two%input_one
    replace2 = remainder2 % input_one
    remainderZero= True
    print(replace2)
      
counter+=1


