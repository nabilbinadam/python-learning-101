"""
You are given an integer array height where height[i] 
represents the height of a vertical line at index i. 
Find two lines that together with the x-axis form a container that holds the
 most water. 
Return the maximum amount of water a container can store.

"""
height = [1,8,6,2,5,4,8,3,7]

def calculatemax(height):

    sum=0 
    left= 0
    right= len(height)
    while right<left:
        sum = height[left]+height[right]


        if sum<
 