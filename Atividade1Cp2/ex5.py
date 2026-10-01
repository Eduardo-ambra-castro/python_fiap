import os
os.system("cls")

regiao = input("Digite a região: ").strip().lower()
valor = float(input("Digite o valor da compra: R$ "))

match regiao:
   case "norte" | "nordeste":
       if valor >= 200:
           frete = 0
       if valor < 200:
           frete = 30

   case "sul" | "sudeste":
       if valor >= 200:
           frete = 0
       if valor < 200:
           frete = 20
           
   case _:
       print("Região inválida!")
       frete = None
if frete is not None:
   print(f"Região: {regiao}")
   print(f"Valor da compra: R$ {valor:.2f}")
   print(f"Frete: R$ {frete:.2f}")