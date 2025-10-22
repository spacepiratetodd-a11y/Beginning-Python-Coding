#import random must be at the top to generate random integers in the file
import random

#the random.randint will generate the numbers, the 1 and 6 in the parantheses define the range
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

#The or is conditional that checks if either condition is true
if die1 + die2 == 7 or die1 + die2 == 11:
    print(f"You win! You rolled a {die1} and a {die2}.")

    # Nested if with an else condition below
elif die1 == die2:
    if die1 == 6 and die2 == 6: #and checks if both conditions are true simultaneously
        print(f"Jackpot! You rolled two 6s!")
    else:
        print(f"Doubles! You win! You rolled two {die1}s.") 
        
#Final else condition if none of the above conditions are met        
else:
    print(f"Not a winner :( You rolled a {die1} and a {die2}.") 