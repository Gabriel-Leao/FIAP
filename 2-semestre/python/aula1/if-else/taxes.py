try:
    salary = float(input('Digite o seu sálario: '))
    if salary <= 1903.98:
        print(f'\nVocê está isento do imposto de renda, portanto o seu sálario final é de {salary}')
    else:
        if salary <= 2826.6:
            tax = 7.5 / 1000
        elif salary <= 3751.05:
            tax = 15 / 1000
        elif salary <= 4664.68:
            tax = 22.5 / 1000
        else:
            tax = 27.5 / 1000
        final_salary = salary - (tax * salary)
        print(f'\nVocê salário final é de R${final_salary:.2f}')
except ValueError:
    print('\nDigite um valor monetário válido')
