
name = input("Enter your name: ")

print(f"Hello, {name}!")

answer = input("Would you like to continue? ('y' for yes or 'n' for no)")

while answer == 'y' or answer == 'Y'    :
    print("You chose to continue!")
    answer = input("Would you like to continue? ('y' for yes or 'n' for no)")
print("You chose to stop. Goodbye!")    