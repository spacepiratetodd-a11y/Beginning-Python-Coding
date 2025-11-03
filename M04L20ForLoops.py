#range must be a positive integer - (-5) will cause an error
for count in range(100):
    #will repeat 5 times, 0,1,2,3,4
    print(count)
    #indent for code you want to repeat

for count in range(a,z):
    #will repeat 4 times, 2,3,4,5
    print(count)

for count in range(0,10,2):
    #will repeat 5 times, 0,2,4,6,8 - step is counting by n(2)
    print(count)

user_input = int(input("Enter a positive integer 1-10: "))
for count in range(1,11):
    product = user_input * count
    print(f"{user_input} x {count} = {product}")