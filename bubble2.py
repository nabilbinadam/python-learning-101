data = [5,4,7,3,9,1]


def bubble(data):
    length=len(data) # will return int 
    for i in range(length) :  # accessing index [0,1,2,3,4,5]
        

        for j in range(i+1-1,length):
            #print(data[j])
            if data[j]<data[i]:
                data[j],data[i]= data[i],data[j]
                print(data)




bubble(data)