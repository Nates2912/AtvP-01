import os
os.system("cls")

#Big Test 7!!!

product  = input("Product:")
quant  = int(input("Cart: "))
price  = float(input("Price: "))

total = price * quant

#process

if quant <= 5 : 
    print(f"You bought {quant} {product}.")
    disc = total * 0.02
   
elif quant > 5 and quant <= 10:
    print(f"You bought {quant} {product}.")
    disc = total * 0.03
    
else:
    print(f"You bought {quant} {product}.")
    disc = total * 0.05

totalfin = total - disc

print ("")

print(f"\n Your total is: {totalfin:.2f}")