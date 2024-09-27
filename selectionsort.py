
data= [6,5,2,5,8,3]



#def selection(data):

length= len(data)
for i in range(length):
        min = data[i]
        #print(min)

        for j in range(min+1,1):
                if data[j]< min:
                        data[j],min = min,data[j]

                        print(j)









    

#selection(data)