user_input = [5,4,7,3,9,1]



def bubblesort(user_input):
    #breakdown step in small step 
    # Computer is stupid.
    # tell the computer to loop trough the list .
    # tell the computer to compare index 1 and index 2.
    # tell the computer if index 1 is greater than 2 then swap the element.
    # tell the computer to do it untill the all condition is statisfy
    n= len(user_input)   # akan return length integer utk panjang list tu
    for i in range(n): # i = 5 (index)
        for j in range(0,i-1):
            if user_input[j]> user_input[j+1]:
                user_input[j],user_input[j+1]=user_input[j+1],user_input[j]
                return user_input

            
 
            
         




print(bubblesort(user_input))




            