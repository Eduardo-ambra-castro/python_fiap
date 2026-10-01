import os
os.system("cls")

valor = float(input("Digite o valor da compra: "))

if valor < 100: 
 print("Não recebe desconto")
 
elif valor <= 100 or valor > 300:
 print("Desconto aplicado 5%")
 print(f"Valor final R$ {valor * 0.95:.2f}")

elif valor <= 300 or valor > 500:
 print("Desconto aplicado 10%")
 print(f"Valor final R$ {valor * 0.90:.2f}")

elif valor <= 500:
 print("Desconto aplicado 15%")
 print(f"Valor final R$ {valor * 0.85:.2f}")

