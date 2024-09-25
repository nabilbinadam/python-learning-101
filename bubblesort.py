

data = [9,7,5,3,2,1]

def bubblesort(data):
    n = len(data)
    for i in range(n): # access the element of index 
        for j in range(0,n-i-1):
              if data[j]>data[j+1]:
                   data[j],data[j+1]=data[j+1],data[j]
                   print(data)


print(bubblesort(data))                 