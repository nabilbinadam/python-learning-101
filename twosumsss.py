"""

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

"""

data = [2,7,11,15]
target= int(input("insert target:"))

length = len(data)
for numbers in data:
    i=numbers
    if data[i] + data[i+1] == target:
        print(data[i],data[i+1])

    else: 
        print("no target")


