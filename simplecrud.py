band=[]


print("MENU")
print("1 CREATE NAME :",) 
print("2 DELETE NAME :",) 
print("3 EDIT NAME :",) 
print("4 View NAME")

user_choice= int(input("Your Choice?:"))
def Menu (user_choice,user_input):
   if user_choice == 1:
      create(user_input)
    
   elif user_choice==2:
       delete()

   elif user_choice == 3:
       edit()

   elif user_choice == 4 :
       view()

   else : 
      print("program exit ")  

def create():
 user_input=print(str(input("insert Band Name:")))
 band.append(user_input)
 print("add success")
 print(band)

def view():
    #read list
    for bands in band:
      if bands in band :
        print(band)
    



def edit():
    # which index to update
    # ask user what input to update
    # append? band[]
    user_input=input(str("choose index to edit:"))
    user_input[create()]

    

def delete () :       

   pass 








Menu(user_choice)

  

