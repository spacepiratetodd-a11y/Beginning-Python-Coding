#Create input prompts to have the user input the values for the variables.
name = input("What is your name? ")
hobby = input("What is your hobby? ")
yearOfBirth = input("What year were you born? ")
currentYear = input("What is the current year? ")

#Creat f-strings to display the input values for the variables.
print(f"Hello, {name}!")
print(f"I also enjoy {hobby}.")

#Calculate the user's age using Python acceptable operations and display it as a value.
print(f"You are {int(currentYear) - int(yearOfBirth)} years old.")
