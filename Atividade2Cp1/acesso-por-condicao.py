import os
os.system("cls")

idade = float(input("Idade:"))
autoriza = str(input("Possui autorização (S/N):"))

if idade >= 18 and autoriza == "s":
    print("Acesso permitido.")
else:
    print("Acesso negado")