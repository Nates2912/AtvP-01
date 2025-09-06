import os
os.system("cls")

#Big Test 10!!!

print("""
Combustível	Quantidade Vendida	Desconto por Litro
Álcool      Até 25 litros	    10%
Álcool   	Acima de 25 litros	20%
Gasolina	Até 25 litros	    15%
Gasolina	Acima de 25 litros	30%
      """)

liters = float(input("Liters: "))
fuel = input("Type of fuel (A-alcohol, G-gasoline): ").upper()

priceal = 3.79
pricega = 6.59

match fuel:
    case "A":  
        if liters <= 25:
            disc = 0.10
        else:
            disc = 0.20
        total = liters * priceal * (1 - disc)

    case "G":  
        if liters <= 25:
            disc = 0.15
        else:
            disc = 0.30
        total = liters * pricega * (1 - disc)
        
    case _:   
        print("Invalid type!")
        total = None
        disc = 0
        fuel_name = "Unknown"

        if total is not None:
            print(f"\nYou bought {liters:.2f} liters of {fuel},")
            print(f"With a discount of {disc*100:.0f}%!")
            print(f"How mch you ahve to pay: R${total:.2f}")