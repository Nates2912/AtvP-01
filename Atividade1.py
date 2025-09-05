#Cleaning the terminal
import os
os.system("cls")

#Big test!!!

A = int(input("Type the first number: "))
B = int(input("Type the second number: "))
C = int(input("Type the third number: "))

result = A + B 

if A + B > C:
    print(f"{C} is smaller than {result}!")
else:
    print(f"{C} is bigger than {result}!")