def twoSum(self, nums, target):
        length= len(nums)  #will return integer
        
        for i in range(length):  # accessing index in i
            number_one = i 

            for j in range(i+1,length):   # accessing i+1
                number_two =j 

                if nums[i] + nums[j]== target:
                    print(nums[i],nums[j])


nums= [1,4,6,7,8]
target=  5
twoSum(nums,target)                    

