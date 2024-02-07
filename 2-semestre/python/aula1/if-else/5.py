try:
    numbers = [
        int(input('Digite um número inteiro: ')),
        int(input('Digite um número inteiro: ')),
        int(input('Digite um número inteiro: '))
    ]
    numbers.sort()

    print(f'\nOs números em ordem crescente: {numbers}')
except ValueError:
    print('\nPor favor, digite um número inteiro')
