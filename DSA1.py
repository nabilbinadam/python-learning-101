data= "abcabcabb"


def sliding(data):


    maxs=0
    left=0
    dic=set()

    for right in range(len(data)):
        while data[right] in dic:
            dic.remove(data[left])
            left+=1
        dic.add(data[right])    
        maxs =max(maxs,right-left+1)  
    return maxs
    

print(sliding(data))   


        