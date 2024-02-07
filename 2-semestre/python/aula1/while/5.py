n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))

while n1 < n2:
    print(n1, end=' ')
    n1 += 1

while n2 < n1:
    print(n2, end=' ')
    n2 += 1
