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
    r=0
    l=0
    for (i,j) in range(length):
        r=i
        l=j+1
        
        print(r)
        print(l)


slide(data,k)