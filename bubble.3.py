data= [1,2,4,6,7,8,2]
def bubblesort(data): 
    #access the index 
    length = len(data)# 7
    for i in range(length): # 0123456
        
        for j in range(length-i-1):  # this is the key of the question 
            print(j)
            if data[i]<data[j]:
                data[i],data[j]=data[j],data[i]
                
                                             


bubblesort(data)
# 7-0-1 = 6 
# 6-0-1= 5
# 5-0-1=4
# 4-0-1=3
# 3-0-1=2
# 2-0-1=1
# 1-0-1=0
  