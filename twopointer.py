"""

Description: Given a 1-indexed array of integers 
numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number.
 Return the indices of the two numbers (1-indexed).
Example:
Input: numbers = [2, 7, 11, 15], target = 9
Output: [1, 2] (because numbers[0] + numbers[1] = 2 + 7 = 9)


"""
data= [2,7,11,15]
target=9
counter = 0
def twosumpointer(data,target):
    left = 0
    right = len(data) - 1
    counter=0
    while left < right:
        sum=data[left]+ data[right]
        if sum== target:
            print(data[left],data[right])

        elif sum != target:
            counter+=1

        else:
            print("no value")    
   


          



twosumpointer(data,target)