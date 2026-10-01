import os
os.system("cls")

num = int(input("Digite a quantidade de minutos: "))

hras = num //60
mints = num % 60
print(f"Tempo: {hras}h{mints}m")