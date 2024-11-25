data = [2,7,11,15]
target = 13

def twopoint(data,target):
    left=0
    right = len(data)-1 

    while right>left:
        sum= data[right]+data[left]

        if sum == target:
            return (data[right],data[left])
        elif sum<target:
            left+=1
        else:
            right-=1

print(twopoint(data,target))