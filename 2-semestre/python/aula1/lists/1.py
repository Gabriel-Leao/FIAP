numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]

qty_odd = 0
qty_even = 0

'''for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        qty_par += 1
    else:
        qty_impar += 1
'''

for number in numbers:
    if number % 2 == 0:
        qty_odd += 1
    else:
        qty_even += 1

print(f'Na lista tem {qty_odd} números pares e {qty_even} números impares.')
