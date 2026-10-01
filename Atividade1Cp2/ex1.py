import os
os.system("cls")

dia = int(input("Digite um dia de 1 a 7: "))

match dia:
    case 1:
        print("Domingo")
  
    case 2:
        print("Segunda")
  
    case 3:
        print("Terça")

    case 4:
        print("Quarta")
  
    case 5:
        print("Quarta")
  
    case 6:
        print("Quarta")

    case 7:
        print("Quarta")
    
    case _:
        print("Dia inválida")