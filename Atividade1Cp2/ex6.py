import os
os.system("cls")

tipo = input("tipo de pedido: ").strip().lower()
prioridade = int(input("número de prioridade: (1, 2 ou 3) "))

match (tipo, prioridade):
    case ("troca" | "devolução", 1):
        print("pós-venda. atendimento: instantaneo.")

    case ("troca" | "devolução", 2):
        print("pós-venda. tendimento: até 4 horas.")

    case ("troca" | "devolução", 3):
        print("pós-venda. atendimento: até 1 dia útil.")

    case ("suporte", 1):
        print("atendimento: instantaneo")

    case ("suporte", 2):
        print("atendimento; até 4 horas.")

    case ("suporte", 3):
        print("atendimento: até 1 dia útil.")

    case _:
        print("info inválida")
