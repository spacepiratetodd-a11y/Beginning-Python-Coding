import random

password_number = int(input("Enter the number of passwords to generate: "))
password_length = int(input("Enter the length of each password: "))

choices = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
print(random.choices(choices) * password_length)