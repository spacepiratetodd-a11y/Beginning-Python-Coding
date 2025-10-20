import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

if die1 + die2 == 7:
    print(f"Sevens! You win! You rolled a {die1} and a {die2}.")
elif die1 + die2 == 11:
    print(f"Elevens! You win! You rolled a {die1} and a {die2}.")
    
    # Nested if below
elif die1 == die2:
    if die1 == 6 and die2 == 6:
        print(f"Jackpot! You rolled two 6s!")
    else:
        print(f"Doubles! You win! You rolled two {die1}s.") 
else:
    print(f"Not a winner :( You rolled a {die1} and a {die2}.") 