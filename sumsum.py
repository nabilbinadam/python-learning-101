
data = [3, 4, 5, [5], ["8"], [[[[[8]]]]]]

def checksum(data):

    counter = 0

    for item in data :
        #check if number
        if isinstance(item,int):
            counter+=item

        elif isinstance(item,str) and item.isdigit():
            counter+=int(item)

        elif isinstance(item,list):
            counter+=checksum(item)    
    
    return counter              





print(checksum(data))