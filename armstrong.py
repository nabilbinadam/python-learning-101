user_input = int(input("Insert Numbers Here: "))
input_string = str(user_input)
squared=0
for  input in input_string :
  squared = squared + int(input**3)

if (squared == user_input):
  print("this is an armstrong Number")

else : 
  print("this is not an armstrong number")  