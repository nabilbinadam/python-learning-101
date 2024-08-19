'''

**Problem 11: Laboratory Problem**

A laboratory technician always needs to prepare various solutions.

Coming Sunday, he has to create a 20-liter solution that is 35% 
salt by mixing two available solutions. One solution (A) is 25% salt, and the other solution (B) is 50% salt. 
How many liters of each solution are required to achieve the desired concentration?

Coming Monday, he has to create an 8-liter solution that is 25% 
sugar by mixing two available solutions. One solution (A) is 15% sugar,
and the other solution (B) is 40% sugar. How many liters of each solution
are required to achieve the 
desired concentration?

Write a simple, generic Python program to assist the laboratory 
technician. The program must take all these numbers (20 liters, 35, 25, 50) 
as input and calculate the required liters of each solution and print them.
Please note that the same program must work for the second problem as well (8 liters, 25, 15, 40).

The maximum stock for solution (A) and solution (B) is always 3 liter only. 
After calculating/printing the required quantity of A and B, throw proper message. 
For example, required quantity of solution (A) is less than 3 liter say "Solution (A) is available can proceed".
If required quantity of solution (B) is greater than 3 liter say "Solution (B) is not available, please order 
1.3 liter now".
'''

#initilize input 
solutionOne = int(input("Insert Input "))
solutionTwo= int(input("Insert Input "))