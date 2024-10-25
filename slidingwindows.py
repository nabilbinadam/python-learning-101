"""

Problem: Maximum Sum of Subarray of Size K
Description: Given an array of integers and an integer K, find the maximum sum of any contiguous subarray of size K.
Example:
Input: arr = [2, 1, 5, 1, 3, 2], K = 3
Output: 9 (the subarray [5, 1, 3] has the maximum sum)

"""

data= [2,1,5,1,3,2]
k = 3 

def slide(data,k):
    length=len(data)
    for i,j in range(length):
        print("this is I:",i)
        print("this is J:",j)

