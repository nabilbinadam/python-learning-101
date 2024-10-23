"""

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

"""

data = [2,7,11,15]
target = 9
def twosum(data,target):
    length= len(data)

    for i in range(length):
        

        for j in range(i):

            if data[i]+ data[j+1] == target:

                print("Correct")
                
            

twosum(data,target)

