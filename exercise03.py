#take age as input
# age less then 10 is children  (age<10)
# age greater than or equals to 10 and less then 18 is minor  (age=>10 and age<18)
# age greater than or equals to 18  and less than 21 is teenager   (age=>18 and age<21)
# age greater than or equals to 21  and less than 60 is adult   (age=>21 and age<60)
# age greater than or equals to 60 and above is Senior      (age=>60)
"""
age = int (input("enter your age"))

if age < 10:
    print("You are a child")
elif 10 <= age < 18:
    print("You are a minor")
elif 18 <= age <= 21:
    print("You are a teenager")
elif 21 < age <= 60:
    print("You are an adult")
else:
    print("You are a senior")

"""

age = int(input("what is your age"))
print ("you are a kid :",age) if (age<10) \
else print("you are a minor:",age) if (age>=10 and age<=18) \
else print("you are a teenager:",age) if (age>=18 and age<=21) \
else print("you are a adult:",age) if (age>=21 and age<=60) \
else print("you are a seniorr:",age) 





