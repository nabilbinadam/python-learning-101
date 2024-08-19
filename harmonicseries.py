'''
Write a program that calculates the sum of the first n terms of 
the harmonic series. Take the n as Input.

Hn = 1 + 1/2 + 1/3 + 1/4 .... + 1/n
'''

n = int(input("Insert number :"))

sum=0
for x in range(1,n+1):
    
    sum+=x/2
print("this:",'sum',sum)   
    
