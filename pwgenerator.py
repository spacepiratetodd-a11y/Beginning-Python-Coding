import random

password_number = int(input("Enter the number of passwords to generate: "))
password_length = int(input("Enter the length of each password: "))

choices = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'

password = ''
for count in range(password_length):    
    password += random.choice(choices)
else: #break the for loop to only generate one password
    print(password) #print only one password