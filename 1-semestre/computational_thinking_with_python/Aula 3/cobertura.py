coberturas = ["cheddar", "queijo extra", "peperoni"]

try:
    cobertura = str(input("Digite a cobertura desejada: ")).lower()

    if cobertura in coberturas:
        print(f"{cobertura} adicionado a sua pizza")
    else:
        print("não temos essa cobertura")
except ValueError:
    print("Por favor digite apenas letras")
except Exception as error:
    print(error)

# if 'frango' in coberturas:
#     print("Adicione frango")
# if 'queijo extra' in coberturas:
#     print("Adicione queijo extra")
# if 'peperoni' in coberturas:
#     print("Adicione peperoni")
