import os
os.system("cls")

#Big Test 7!!!

product  = input("Product:")
quant  = int(input("Cart: "))
price  = float(input("Price: "))

quant = price * quant

#process

if quant <= 5 : 
    print(f"You bought {quant} {product}.")
    disc = price * 0.02
    total = quant  - disc
elif quant > 5 and quant <= 10:
    print(f"You bought {quant} {product}.")
    disc = price * 0.03
    total = quant  - disc
elif quant > 10:
    print(f"You bought {quant} {product}.")
    disc = price * 0.05
    total = quant  - disc
else:print(f"You bought {quant} {product}.")
    

#exit

print ("")

print(f"\n Your total is: {total:.2f}")