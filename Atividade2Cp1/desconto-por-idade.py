import os
os.system("cls")

idade = float(input("Sua idade:"))

if idade >= 60 or idade <= 12:
    print("Tem direito ao desconto.")
else:
    print("Não tem direito ao desconto")