"""

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the 
longest contiguous subarray 
with an equal number of 0 and 1

[0,1,5,3]
the longest is [0,5]
"""
input =[0,1]


def ContArray (input):
    length= len(input)

    for i in range(length):
       
        arrCont=int(i)

        print(arrCont)


ContArray(input)