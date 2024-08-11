# value = input('Please enter a value:\n') #message to user

# print(value)
import sys
import random # module for the computer to choose at random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
playerchoice = input("Enter.. \n1 for Rock \n2 for Paper \n3 for Scissors: \n\n")

#Applying control flow

# if 1 > 2:
#     print('do something') #this is a code block 
player = int(playerchoice)

if player < 1 | player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("")
print(" You chose " + str(RPS(player)).replace('RPS.', ' ') + ".")
print(" Python chose " + str(RPS(computer)).replace('RPS.', ' ' )+ ".")
print("")

if player == 1 and computer == 3:
    print("🥳You win!")
elif player == 2 and computer == 1:
    print("🥳You win!")
elif player == 3 and computer == 2:
    print("🥳You win!")
elif player == computer:
    print("😲Tie!")
else:
    print("Python wins!, you suck asss💀")
