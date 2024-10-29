

data = [3, 4, 5, [5], ["8"], [[[[[8]]]]]]

#isInstance()
#check if its number
#check if string
#check if "[bracket]"

def sumofdata(data):
    
    counter = 0

    for item in data:
        if isinstance(item,int):
            counter+=item
        elif isinstance(item,str) and item.isdigit():
            counter+=int(item)

        elif isinstance(item,list):

            counter+=sumofdata(item)

    return counter        










print(sumofdata(data))