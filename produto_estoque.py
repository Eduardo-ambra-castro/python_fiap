import os
os.system("cls")

n = input("Nome do produto: ")
qtd = float(input("Digite o preço unitario: "))
pu = float(input("Digite a quantidade: "))
desc = float(input("Digite o precentual de desconto: "))

vb = (pu) * (qtd)
desC = (vb) * (desc) / 100
vf = (vb) - (desC)
print(f"Produto: {n}")
print(f"Valor bruto: R${vb} ")
print(f"Desconto: R${desC} ")
print(f"valor final: R${vf}")

