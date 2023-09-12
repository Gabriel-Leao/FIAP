velocidade = int(input("digite a velocidade em que estava em km/h: "))

if velocidade > 80:
    print(f"O valor da multa é R${(velocidade - 80) * 5:.2f}")
else:
    print("Você está dentro do límite")
