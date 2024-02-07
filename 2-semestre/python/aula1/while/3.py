pop_a = 80000
pop_b = 200000
years = 0

while pop_a < pop_b:
    pop_a *= 1.03
    pop_b *= 1.015
    years += 1


print(f'Demorou {years} anos para a populaçâo do país a passar o pais b. Hoje o pais a tem {pop_a} habitante e o pais b = {pop_b}')
