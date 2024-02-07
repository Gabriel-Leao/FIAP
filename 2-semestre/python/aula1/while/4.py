qty = 0
sum = 0

while qty < 5:
    num = float(input(f'Digita o {qty + 1} número: '))
    sum += num
    qty += 1

average = sum / qty
print(f'A média foi {average} e a soma foi {sum}')
