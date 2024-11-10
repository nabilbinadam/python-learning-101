
data = [3, 4, 5, [5], ["8"], [[[[[8]]]]]]


def checkInput(data):

    sum = 0 
    for item in data:
    
        if  isinstance(item,int):
            sum+=item

        elif  isinstance(item,str) and item.isdigit():

            sum+=int(item)

        elif isinstance (item,list):
            sum+=checkInput(item)
    return sum              


print(checkInput(data))