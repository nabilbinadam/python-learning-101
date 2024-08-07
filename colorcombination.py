pantcolors = ["Black","Brown","Blue"] 
shirtcolors = ["White","Red","Blue"]
combination= []
#find the colour combination 

for shirtcolor in shirtcolors :
    for pantcolor in pantcolors:
        if(shirtcolor != pantcolors):
         combination.append((shirtcolor,pantcolor))



print (combination)

combinations = [(shirtcolor,pantcolor) for shirtcolor in shirtcolors for pantcolor in pantcolors if (pantcolor!=shirtcolor)]

print("this is the new combination",combinations)