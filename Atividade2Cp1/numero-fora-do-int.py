import os
os.system("cls")

numero = int(input("Digite um número inteiro: "))

if numero < 1 or numero > 100:
    print("O número está fora do intervalo de 1 a 100.")
else:
    print("O número está dentro do intervalo de 1 a 100.")