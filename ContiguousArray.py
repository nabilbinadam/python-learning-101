"""

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the 
longest contiguous subarray 
with an equal number of 0 and 1

"""
input =[0,1]


def ContArray (input):
    length= len(input)

    for i in range(length):
       
        arrCont=int(i)

        if 