
class Character:

    def __init__(self,name,gender,type,attack):
        
        self.name= str(name) 
        self.gender=str(gender)
        self.type=str(type)
        self.attack=int(attack)

    def display(self):
        print(self.name)
        print(self.gender)
        print(self.type)  
    def fight(self):

        char1=self.attack
        char2=self.attack



char1= Character("Karim","Male","Warrior")
char2= Character("Azula","Female","Archer")

char1.display()
print("_-----------------_")
char2.display()