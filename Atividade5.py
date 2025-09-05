#Para limpar o terminal
import os
os.system("cls")

#imput do usuario
numero1 = float (input("Digite um numero: "))
print("")
numero2 = float (input("Digite um numero: "))
print("")

#como as contas funcionam

math = input("Choose your operator: ")

soma = numero1+numero2
subtracao = numero1-numero2
multiplicacao = numero1*numero2
divisao = numero1/numero2

match math:
    case "sum":
        print(f"Sum: {soma}")
    case "sub":
        print(f"Subtraction {subtracao}")
    case "mult":
        print(f"Multiplication: {multiplicacao}")
    case "div":
        print(f"Division: {divisao}")

