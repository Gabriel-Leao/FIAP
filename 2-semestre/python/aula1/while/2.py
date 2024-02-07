while True:
    name = str(input('Digite o seu nome: '))
    if len(name) > 3:
        break
    else:
        print('Nome inválido')
        continue

while True:
    age = int(input('Digite a sua idade: '))
    if 0 <= age <= 150:
        break
    else:
        print('Idade inválida')
        continue

while True:
    salary = float(input('Digite o seu sálario: '))
    if salary > 0:
        break
    else:
        print('Sálario inválido')
        continue

while True:
    sex = str(input('Digite o seu sexo [M] [F]: ')).upper()
    if sex == 'M' or sex == "F":
        break
    else:
        print('Sexo inválido')
        continue

while True:
    marital_status = str(input('Digite o seu estado civil [S] [C] [V] [D]: ')).lower()
    if marital_status == 's' or marital_status == 'c' or marital_status == 'v' or marital_status == 'd':
        break
    else:
        print('estado civil inválido')
        continue

print(f'Olá {name}, você tem {age} anos, recebe R${salary:.2f} de sálario, seu sexo é o {sex} e seu estado cívil é {marital_status}')
