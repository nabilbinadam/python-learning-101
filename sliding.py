
data = "abcabcbb"


def sliding (data):
    char=set()
    left=0
    sum=0

    for right in range(len(data)):
        while data[right] in char:
            char.remove(data[left])
            left+=1
        
        char.add(data[right])
        sum=max(sum,right-left+1)
    return sum 


        


print(sliding(data))