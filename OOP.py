class Patient:
    def __init__(self, firstname, lastname, icnumber):
        print("Object created successfully")
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = icnumber
        self.medicinesprices = []

    def info(self): 
        print("firstName:", self.firstname)
        print("lastName:", self.lastname)
        print("icnumber:", self.icnumber)   

    def doPayment(self):
        total = 0
        for price in self.medicinesprices:
            total += price
        return total

# Creating Patient objects with required parameters
peter = Patient("Peter", "Park", 2103890128)     
anthony = Patient("Anthony", "Smith", 301298312)     
mike = Patient("Mike", "Jones", 405920384)     

print(type(mike))    

# Setting properties for peter
peter.medicinesprices = [6.20, 12.80, 15.00, 40.00]

# Printing amount to be paid
print("Amount to be paid:", peter.doPayment())

# Optionally, print the info for Peter
peter.info()


karim = Patient("Karim","Benzema",10292837)
karim.info()


