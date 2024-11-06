
class Car : 

    def __init__(self,type,colour,plate):
        
        self.type=type
        self.colour=colour
        self.plate=plate
        self.carprice=[]
        print("car created successfully")


    def showcase(self) :

        print(self.colour)
        print(self.type)
        print(self.plate)
        print(self.carprice)
        
    
    def calculateprice(self):
        sum=0
        for price in self.carprice:
            sum+=price

            return sum 

User_1=Car("4wd","red","blb512")
User_2=Car("mpv","blue","blb522")
User_3=Car("sedan","green","blb532")


User_2.carprice= [1234]
User_1.carprice= [1634]
User_3.carprice= [1244]
User_1.showcase()
print("-----------------------")
User_2.showcase()
print("-----------------------")
User_3.showcase()
print("-----------------------")

total_price = User_1.carprice + User_2.carprice + User_3.carprice

def kira(total_price):
    sum=0
    length = len(total_price)
    for price in range(length):
        sum+=total_price[price]

    return sum      
    

print(kira(total_price) )
    
  

