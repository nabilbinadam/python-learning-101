'''
Write a program that randomly generates a number between 1 and 100. 
The user has to guess the number. 
After each guess, the program tells 
the user whether the guess is too high, 
too low, or correct. 
The game continues until the user guesses the correct number.

To generate random number use random module

import random

random.randint(1,3)

'''
import random 

user_guess = int(input("Guess the number :"))
NpcGenerate= random.randint(1,100)

if(user_guess==NpcGenerate):print("You are correct","The answer is:",NpcGenerate)
elif(user_guess>NpcGenerate):print("Too High" ,"The answer is:",NpcGenerate)
elif(user_guess<NpcGenerate):print("Too Low","The answer is:",NpcGenerate)
