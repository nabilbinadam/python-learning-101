
data = [3, 4, 5, [5], ["8"], [[[[[8]]]]]]

def sumodata(data):

    #check number
    counter=0
    for item in data:

        if isinstance(item,int):
            counter+=item
        elif isinstance (item,str) and item.isdigit():
            counter+= int(item)

        elif isinstance(item,list):
            counter+=sumodata(item)

    return counter     










print(sumodata(data))