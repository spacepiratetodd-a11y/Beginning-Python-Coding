import random

name = input("Welcome Human! Tell me your name: ")
print(f"Hello, {name}! Let's play Rock, Paper, Scissors.") 

choices = ['rock', 'paper', 'scissors']

choice = input("Take your pick (r)ock, (p)aper, or (s)cissors: ")

winCountName = 0
loseCountName = 0
tieCountName = 0

winCountComputer = 0
loseCountComputer = 0
tieCountComputer = 0

computer = random.choice(choices)
while winCountName < 3 and winCountComputer < 3:
    if name == "r" or "R":
        choice = "rock"
        if computer == "rock":
            print(f"Both players selected rock. It's a tie!")
            tieCountName += 1
            tieCountComputer += 1

        if computer == "scissors":
            print(f"Rock smashes scissors! You win! Computer selected {computer}.")
            winCountName += 1
            loseCountComputer += 1

        elif computer == "paper":
            print(f"Paper covers rock! You lose. Computer selected {computer}.")
            loseCountName += 1
            winCountComputer += 1

    elif name == "p" or "P":
        choice = "paper"
        if computer == "paper":
            print(f"Both players selected paper. It's a tie!")
            tieCountName += 1
            tieCountComputer += 1

        if computer == "rock":
            print(f"Paper covers rock! You win! Computer selected {computer}.")
            winCountName += 1
            loseCountComputer += 1

        elif computer == "scissors":
            print(f"Scissors cuts paper! You lose. Computer selected {computer}.")
            loseCountName += 1
            winCountComputer += 1

    elif name == "s" or "S":
        choice = "scissors"
        if computer == "scissors":
            print(f"Both players selected scissors. It's a tie!")
            tieCountName += 1
            tieCountComputer += 1

        if computer == "paper":
            print(f"Scissors cuts paper! You win! Computer selected {computer}.")
            winCountName += 1
            loseCountComputer += 1

        elif computer == "rock":
            print(f"Rock smashes scissors! You lose. Computer selected {computer}.")
            loseCountName += 1
            winCountComputer += 1
if winCountName == 3:
    print(f"Congratulations {name}, you are the overall winner!")
elif winCountComputer == 3:
    print("The computer is the overall winner! Better luck next time.")
