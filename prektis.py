

data  = {

    "Name":"Karim",
    "Id":"92383",
    "User_type":"Admin",
    "Date_created":"March"

}


print(data["Name"])
print (data.values())
print(len(data))
for date in data : 
    if "Name" in date:

       print("Access Granted")