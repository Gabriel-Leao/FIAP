a = 0
b = 1
c = a + b
qty = 0

while qty <= 10:
    c = a + b
    print(f'{a} + {b} = {c}')
    a = b
    b = c
    qty += 1
