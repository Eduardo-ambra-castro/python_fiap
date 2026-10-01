import os
os.system("cls")

idade = float(input("Digite a sua idade: "))

if idade < 0: 
 print("Idade invalida")
 
elif idade <= 0 or idade > 5:
 print("Não paga")

elif idade >= 6 or idade > 12:
 print("Paga R$ 10,00")
 
elif idade >= 13 or idade > 59:
 print("Paga R$ 25,00")

elif idade >= 60:
 print("Paga R$ 12,00")
