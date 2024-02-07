brands = ["volksvagen", "chevrolet", "audi", "fiat", "volvo"]

car = str(input("Digite qual a marca do seu carro: ")).lower()

if car in brands:
    for brand in brands:
        if car == brand:
            print(f"Seu carro está na lista e é da marca {brand}")
            break

else:
    print("Seu carro não está na lista")
