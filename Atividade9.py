#Cleaning the terminal
import os
os.system("cls")

#Big test 9!!!

incm = float(input("Your monthly income: "))
loan = int(input("The desired loan: "))
isnt = int(input("Amount of installments: "))

maxloan = incm * 10
maxisnt = incm * 0.30
prest = loan /isnt

if loan <= maxloan and prest <=  maxisnt:
    print (f"LOAN APPROVED! \n Amount of installments is: R${prest:.2f}" )
else: 
    print ("LOAN REJECTED!")
    if loan > maxloan: 
        print ("It exceeds the max of 10x")
    if prest > maxisnt:
        print ("It exceeds the max of 30%")