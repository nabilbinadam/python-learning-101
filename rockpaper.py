'''
Write a program that plays the game of Rock, Paper, Scissors with the user. 
The user makes a choice, the program randomly chooses, 
and the winner is determined.

To generate random number use random module

import random

random.randint(1,3)

'''
#decalre rock paper scissor into variable as integer
#user choose in the form of input = 1 
# win condition for rock > paper=lose , rock>scissor else draw
# win condition for paper >rock =win , paper>scissor=lose else draw. 
# win condition for scissor >rock =lose , paper>scissor=win else draw. 

import random

rock=1
paper=2
scissor=3
#RPS = [rock,paper,scissor]

user_input=int("Rock = 1 , Paper= 2, scissor=3-----Pick one:")

# rock case

rockWin = rock>scissor 
rocklost= rock 