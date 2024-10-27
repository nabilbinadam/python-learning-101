"""

Description: Given a 1-indexed array of integers 
numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number.
 Return the indices of the two numbers (1-indexed).
Example:
Input: numbers = [2, 7, 11, 15], target = 9
Output: [1, 2] (because numbers[0] + numbers[1] = 2 + 7 = 9)


"""
  
data = [2,7,11,15]
target = 9

def twosumpointer(data,target):
    right= data[0]
    left = data[-1]
    while right>left:
        sum = right + left 
        if sum == target :
            print(right,left)

        elif sum != target :
            print(right,left)
    



          



twosumpointer(data,target)