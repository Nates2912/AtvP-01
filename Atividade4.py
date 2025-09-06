#Cleaning the terminal
import os
os.system("cls")

#Big test 4!!!

 
print("""
Fruit   \t   5KG        More than 5KG
Sberry  \t   2,50       R$2,20
Appple  \t   1,80       R$1,50
  """)


basket = int(input("Choose the fruit (1 = strawberry, 2 = apple): "))
kilo = int(input("How many fruits are in your cart: "))


if basket == 1:  
    if kilo <= 5:
        price = 2.50
    else:
        price = 2.20
elif basket == 2: 
    if kilo <= 5:
        price = 1.80
    else:
        price = 1.50
else:
    print("Invalid option.")
    exit()

totalfinal = kilo * price

if kilo > 15 or totalfinal > 25:
    totalfinal *= 0.90 

print(f"\nYou bought {kilo:.2f}kg of {basket}(s) for a total of R${totalfinal:.2f}")