
data= [6,5,2,5,8,3]



def selection(data):
        length= len(data)

        for i in range(length):
            min = i # print element 6,5,2,5,8


        #print(min)

            for j in range(i+1,length): #index

                #print (j)  # j kena generate [5,5,3]
                
                if data[j]<data[min]:

                        min=j
                        #print(j)
                        data[i],data[min]=data[min],data[i]  # swap the element not the index.
                        print(data)
              
                


#same number 
print(selection(data))