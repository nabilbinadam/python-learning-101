"""
Create a class 
Engine with an attribute horsepower. Then, create a
 class Car that has an attribute engine of type Engine
 . Demonstrate aggregation by creating a Car with a Engine object
 , and print the car's horsepower. Demonstrate your understanding 
 of Aggregation, Composition and
   has a relationship in this problem by
     adding all necessary properties and methods.


"""

class Engine : 

    def __init__(self,car):
        self.car=[]
        self.horsepower = {"power":"100hp"}
       
class Car : 

      def __init__(self,Engine):
        Engine=[]   
        self.typeEngine={ 
                  "type": "V-Tech"
            
                }


print(Car.typeEngine("karim"))



