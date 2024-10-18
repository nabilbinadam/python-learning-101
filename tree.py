data = {
    "name" : "nabil" ,
    "adress": "no 6",
    "ic": "043022",
    "phone": "298448",
    "user_type": "admin",

}

info = data.values()
getting = data.items()


data["name"] = "karim"
#print(getting)

if "name" in data :
    print ("yes")