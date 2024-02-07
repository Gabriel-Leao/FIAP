try:
    price = 0.30
    qty_apples = int(input('Digite a quantidade de maças que você quer comprar: '))

    if qty_apples <= 0:
        raise ValueError()
    elif qty_apples < 12:
        final_price = qty_apples * 0.30
    else:
        final_price = qty_apples * 0.25

    print(f'\nO total da sua compra foi R${final_price:.2f}')
except ValueError:
    print('\nPor favor, digite um número a partir de um')
