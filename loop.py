name = input("Enter your name: ")
print(f"Hello, {name}!")

answer = input("Would you like to continue? ('y' for yes or 'n' for no)")

loopCount = 1

while answer == 'y' or answer == 'Y':
    print("You chose to continue!")
    print(f"You have continued {loopCount} times.")
    answer = input("Would you like to continue? ('y' for yes or 'n' for no)")  
    loopCount += 1
print("You chose to stop. Goodbye!")    