

data = [3, 4, 5, [5], ["8"], [[[[[8]]]]]]

def checksum(data):

    counter = 0 


    for item in data:
            if isinstance(item,int):
                counter +=item 

            elif isinstance(item,str) and item.isdigit() :
                
                counter += int(item)   

            elif isinstance(item,list) and item != 0:
                
                counter+= checksum(item)
                  
    return counter









print(checksum(data))