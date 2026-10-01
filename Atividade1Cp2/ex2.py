import os
os.system("cls")

cor = input("Digite a cor: ").strip().lower()

match cor:
    case "verde":
         print("Seguir")
    case "amarelo":
         print("Atenção")
    case "vermelho":
        print("Parar")
    case _:
        print("Cor invalida")