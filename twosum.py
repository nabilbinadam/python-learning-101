def twoSum( nums, target):
        length= len(nums)  #will return integer
        
        for i in range(length):  # accessing index in i
            number_one = i 

            for j in range(i+1,length):   # accessing index i+1
                number_two =j 

                if nums[i] + nums[j]== target:
                    result = nums[i],nums[j]
                    print(result)


nums= [1,4,6,7,8]
target=  7
twoSum(nums,target)      

