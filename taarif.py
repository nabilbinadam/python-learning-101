user_unit= float(input("Insert unit:"))

total_bills = 0
if(user_unit <= 100):
 bill = 0.50 
 total_bills += (user_unit - 100) * 0.50

elif(user_unit <= 200):
 bill = 0.75 
 total_bills += (user_unit - 200) * 0.75

elif(user_unit <= 300):
 bill = 1.20
 total_bills += (user_unit - 300) * 1.20
 
elif(user_unit > 300):
 bill = 1.50
 total_bills += (user_unit - 300) * 1.50

print("Your Total Bills",total_bills)

