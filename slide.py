
data = ["abcabcbb"]
# output will 3

def slidingwindows(data):
    max_length=0
    left=0
    box = set()

    for right in range(len(data)):
        while data[right]  in box:
            box.remove(data[left])
            left+=1
            box.add(data[right])
            max_length = max(max_length, right - left + 1) 
        return max_length           
    
            






print(slidingwindows(data) )