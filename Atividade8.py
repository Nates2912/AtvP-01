import os 
os. system ("cls")

print("""
Code \t Color          Cost
   1 \t Green          R$10,00
   2 \t Blue           R$20,00
   3 \t Yellow         R$30,00
   4 \t Red            R$40,00
""")

cd = input ("Which cd do you want to buy? \n")

match cd:
    case "Green":
        preco = 10
    case "Blue":
        preco = 20
    case "Yellow":
        preco = 30
    case "Red":
        preco = 40
    case _:
        preco = None  # caso não digite nenhuma opção válida

if preco is not None:
    print(f"You chose the {cd} CD, which costs R${preco}")
else:
    print("Invalid CD option.")