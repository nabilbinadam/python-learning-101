
Early_Bird= ['E','e']
Discount= ['D','d']
Vip= ['V','v']
Standard= ['S','s']
Child= ['C','c']
input= str(input("insert ticket:"))

if input in Early_Bird:

    print("Early Bird Ticket")

elif input in Discount:
    print("Discount Ticket")
elif input in Standard:
    print("Standard Ticket")
elif input in Child:
    print("Child Ticket")
elif input in Vip:
    print("Vip ticket")
          