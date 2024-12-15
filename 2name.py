
name ="Sam Jacob"


#get the name
#split the name into two
#Take first initial

def splitName (name):
    split=name.split(" ")
    first_char= split[0][0]
    second_char=split[1][0]
    
    return first_char + second_char
    






print(splitName(name))