price = 0
kwh_qty = 0

while True:
    try:
        kwh_qty = float(input("quantidade de kWh consumida: "))

    except ValueError:
        print("\nPor favor digite apenas números\n")
        continue

    except Exception as error:
        print(f"\nOpa, ocorreu um erro: {error}\n")
        continue

    break

while True:
    try:
        installation_type = int(input("tipo de instalação\n"
                                      "[1] residências\n[2] indústrias \n[3] comércios\n"))

        if installation_type == 1:
            if kwh_qty <= 500:
                price = kwh_qty * 0.5
            else:
                price = kwh_qty * 0.75
            break

        elif installation_type == 2:
            if kwh_qty <= 1000:
                price = kwh_qty * 0.65
            else:
                price = kwh_qty * 0.7
            break

        elif installation_type == 3:
            if kwh_qty <= 5000:
                price = kwh_qty * 0.65
            else:
                price = kwh_qty * 0.7
            break

        else:
            print("\nPor favor, digite um número entre 1 e 3\n")

    except ValueError:
        print("\nPor favor digite apenas números\n")

    except Exception as error:
        print(f"\nOpa, ocorreu um erro: {error}\n")

print(f"Esse mês você terá que pagar R${price:.2f} de energia")
