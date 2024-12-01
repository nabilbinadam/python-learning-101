data = "abcabcbb"

def slidingWindow(data):
    left=0
    char=set()
    maxValue=0

    for right in range(len(data)):
        while data[right] in char:
            char.remove(data[left])
            left+=1
        char.add(data[right])
        maxValue=max(maxValue,right-left+1)
    return maxValue


print(slidingWindow(data))