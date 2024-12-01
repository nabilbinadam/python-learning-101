data= "abcabcabb"


def slidingwindows(data):
    left=0
    char=set()
    maxvalue=0
    

    for right in range(len(data)):
        while data[right] in char:
            char.remove(data[left])
            left+=1 
        char.add(data[right])
        maxvalue=max(maxvalue,right-left +1)
    return maxvalue
    

print(slidingwindows(data))