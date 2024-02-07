dia_semana = input("Digite o dia da semana: ").lower()
dia_mes = int(input("Digite o dia do mês: "))

if (dia_semana != "sabado" or dia_semana != "domingo") and (1 <= dia_mes <= 5):
    print("Você recebera pagamento")
else:
    print("Você nâo receberá pagamento")
