   #python has in built function to take input from user
   # it takes single paramater
   # always return as a string


yourname= input("what is your name:")
print("Goodmorning",yourname) 
print("Goodmorning",type(yourname)) 


principle = float (input('Enter amount(RM):'))

period =   float (input ('enter the ammoung (RM):'))

rate = float ( input ('Enter Amount (%):'))
interest = (principle * period *rate)/100


print ("Total amount needed to be paid (RM):",interest+period)

print (type(interest),id(interest))

