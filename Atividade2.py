#Cleaning the terminal
import os
os.system("cls")

#Big test 2!!!

name = input("Type in your name: ")
gender = input("Type in your gender (M or F): ")
state = input("Type in your civil state (Single or Married): ")

match gender: 
    case "M": 
        print("Male")
    case "F":
        print("Female")
    case _: 
        print("INVALID.")
    

match state: 
    case "Single": 
        print("Single")
    case "Married":
        print("Married")
    case _: 
        print("INVALID.")

if gender == "F" and state == "Married":
    marriedyears = input("For how long you were married?: ")




print(f"Name: {name}")
print(f"Gender: {gender}")
print(f"Civil state: {state}")





