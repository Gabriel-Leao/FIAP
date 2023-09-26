# i = 1
# while True:
#     try:
#         number = int(input("Digite um número para ver sua tabuada: "))
#         multiplo = int(input("Digite o multiplo: "))
#
#         while i <= multiplo:
#             print(f"{number:3} X {i:3} = {number * i:3}")
#             i += 1
#         break
#     except ValueError:
#         print("Por favor digite apenas números inteiros \n")
#         continue

gabarito = ["a", "c", "d"]
questions = 0
pontos = 0

while True:
    try:
        while questions < 3:
            resposta = str(input(f"Digite a resposta da {questions + 1} questão: [a], [b], [c] [d]\n")).lower()
            if resposta == gabarito[questions]:
                pontos += 1
                print("Resposta correta\n")
            else:
                print("Resposta errada\n")
            questions += 1
        if pontos == 0:
            print("Você não fez nenhum ponto")
        elif pontos > 1:
            print(f"Você fez {pontos} pontos")
        else:
            print(f"Você fez {pontos} ponto")
        break
    except ValueError:
        print("Por favor digite apenas letras\n")
        continue
