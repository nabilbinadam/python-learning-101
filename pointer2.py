nums= [1,4,6,7,8]
target=  10

def pointertwo(nums,target):


   left =0
   right = len(nums)-1

   while left<right:
      sum = nums[right]+nums[left]

      if sum == target:
         print(nums[left],nums[right])
         return
      elif sum < target:
         left+=1

      else:
         right-=1
    


    





pointertwo(nums,target)