

class Adress:
        #constructor which run automaticly 
    def __init__(self,street_one,city,state,postcode,country):
        self.street_one = street_one
        self.city = city
        self.state= state
        self.postcode = postcode
        self.country = country



class Customer :
    
    #constructor which run automaticly 
    def __init__(self,firstname,lastname,icnumber):
        self.firstname= firstname
        self.lastname= lastname
        self.icnumber= icnumber
        #customers has many adress
        self.adresses= []
        
class VipCustomer(Customer):
    
    def __init__(self,firstname,lastname,icnumber,discount):
        super().__init__(firstname,lastname,icnumber)
        self.discount = discount
        self.addresses=[]
    
    
               
        
        
peter = Customer("Peter","Parker",1231238) 

adressOne = Adress("No 3","Bangi","Selangor",43650,"Malaysia")       


peter.adresses.append(adressOne)

aida= VipCustomer("Aida,","Jebat",128391283,10)


print(type(aida))
print(type(peter))