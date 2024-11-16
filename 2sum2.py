nums= [1,4,6,7,8]
    #  0,1,2,3,4
target=  5


def sum(nums,target):
    right=len(nums)-1
    print(right)
    left = 0

    while left<right:

        sum = nums[left]+nums[right]

        if sum==target:
            return (nums[left],nums[right])
        
        elif sum < target :
            left+=1 

        else:
            right-=1



print(sum(nums,target))