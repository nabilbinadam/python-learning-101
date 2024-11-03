nums= [1,4,6,7,8]
target=  7


def twopointer(nums,target):
    
    left= 0
    right= len(nums)-1

    while left<right :
        sum=nums[left]+nums[right]

        if sum == target:
            
            return (nums[left],nums[right])
        elif sum <target:
            left+=1

        else :
            right-=1 

       

    



print(twopointer(nums,target))