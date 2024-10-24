

data= [3,5,7,8,10]

target=int(input(""))
def twosum(data,target):

    length=len(data)

    for i in range(length):

        for j in range(i+1):

            if data[i]+data[j]== target:
                print(data[i],data[j])



twosum(data,target)               