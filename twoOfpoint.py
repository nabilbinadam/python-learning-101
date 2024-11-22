data = [2,7,11,15]
target = 13

def sum(data,target):

    left = 0 
    right= len(data)-1

    while right>left:

        sum=data[left]+data[right]

        if sum == target:
            return (data[left],data[right])

        elif sum<target:
            left+=1
            
        else:
            right-=1 


print(sum(data,target))
           
