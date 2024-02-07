try:
    n1 = int(input('Digite um número inteiro: '))
    n2 = int(input('Digite um número inteiro: '))
    n3 = int(input('Digite um número inteiro: '))

    print(f'\nO maior número digitado foi: {max(n1, n2, n3)}')
except ValueError:
    print('\nPor favor, digite um número inteiro')
