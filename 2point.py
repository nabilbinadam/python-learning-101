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
def twopointer(data, target):
    right = len(data) - 1
    left = 0  # This is incorrect; 'left' should be an index, not a value.
    while right > left:
        sum = data[right] + data[left]

        if sum == target:
            print(data[left], data[right])
            return
        elif sum < target:
            left += 1
        else:
            right -= 1


twopointer(data,target)   



    
    
    
    














