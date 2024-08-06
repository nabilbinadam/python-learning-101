
fruits = ("apple","pineapple","mango","grapes")


for fruit in fruits :
    if (len(fruit)== 5 ) :

        print(fruit)



#range will take start index and end index not included 
#iterator object hold more value in the variable
'''
for fruitz in range(0,len(fruits)) : 
    if (len(fruits)==4) :

         print ("false fruits")

         print ((fruitz))
         '''

index = range (0,len(fruits))
for index in range(0,len(fruits)) :
    print (index,fruits[index])