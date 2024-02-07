import math

while True:
    try:
        option = int(input("Digite qual forma geometrica você quer calcular a área\n"
                           "[1] Retângulo\n[2] Quadrado\n[3] Círculo\n"))

        if option == 1:
            base = float(input("Digite a base do retângulo em cm: "))
            height = float(input("Digite a altura do retângulo em cm: "))
            print(f"A área deo retângulo é de {base * height:.2f} cm²")
            break

        elif option == 2:
            lado = float(input("Digite um dos lados do quadrado em cm: "))
            print(f"A área do quadrado é de {lado * lado:.2f} cm²")
            break

        elif option == 3:
            raio = float(input("Digite o raio do circulo em cm: "))
            print(f"A área deo círculo é de {math.pi * raio ** 2:.2f} cm²")
            break

        else:
            print("\nPor favor, digite um número entre 1 e 3\n")

    except ValueError:
        print("\nPor favor digite apenas números\n")

    except Exception as error:
        print(f"\nOpa, ocorreu um erro: { error }\n")
