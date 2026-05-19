# Write a Python program to check whether a number entered by the user is greater than 50 or not. 
# Also, if it is greater than 50, then check whether it is odd or even.

num = int(input("Enter a random number: "))

if num > 50:
    print(f"The number {num} is greater than 50")

    if num % 2 == 0:
        print(f"The number {num} is also even.")
    else:
        print(f"The number {num} is also odd.")
else:
    print(f"The number {num} is less than 50.")