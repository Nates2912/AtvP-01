import os
os.system("cls")

#Start

n1= float (input("Type in the first number: "))
print("")
n2= float (input("Type in the second number: "))
print("")


media= (n1+n2) /2

if media >= 7:
    resultado = "Approved"
elif media > 4.1 and media <5.9:
    resultado = "Summer classes"
else:
    resultado = "Will have to repeat the year."

print(f"Average: {media}")
print("")
print(f"Results: {resultado}")