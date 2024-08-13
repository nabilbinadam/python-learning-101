

#encapsulation
# there are two step for it. 
# make the properties private
#




class Patient:
    def __init__(self, firstname, lastname, icnumber):
        print("Object created successfully")
        self.__firstname = firstname
        self.__lastname = lastname
        self.__icnumber = icnumber
      

    def info(self): 
        print("firstName:", self.__firstname)
        print("lastName:", self.__lastname)
        print("icnumber:", self.__icnumber)   
        
    def getFirstName(self):
        return self.__firstname
    
    def setFirstName(self,firstname,):
         illegalName= ["","something","none"]
         if (firstname not in illegalName) :
             print("ILLEGAL NAME")
             self.__firstname = firstname
    firstname= property(getFirstName,setFirstName)
         
     
peter= Patient("Peter","Parker",847286384)


peter.__firstname= "karim"
peter.info()

peter.setFirstName("something")
peter.info()


peter.setFirstName="mengarut"

print("peter new name :",peter.getFirstName)
