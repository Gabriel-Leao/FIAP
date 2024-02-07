multiplicando = 1

while multiplicando <= 10:
    multiplicador = 1

    print('=' * 20)
    print(f'Tabuada do {multiplicando}: \n')
    while multiplicador <= 10:
        print(f'{multiplicando:2} X {multiplicador:2} = {multiplicando * multiplicador:3}')
        multiplicador += 1
    print('=' * 20)
    
    multiplicando += 1
