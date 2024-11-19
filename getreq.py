
data = [2,7,11,15]
target = 9 


def twopoint(data,target):

    right= len(data)-1  
    left =0

    while right>left:
        sum = data[right]+data[left]

        if sum == target :
            return (data[left],data[right])
        
        elif sum<target:
            left+=1

        else:
            right-=1 


print(twopoint(data,target))