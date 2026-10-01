import os
os.system("cls")

usuario = str(input("Seu usuario:"))
senha = str(input("Sua senha:"))

if usuario == "admin" and senha == "123":
    print("Login realizado com sucesso.")
else:
    print("Login incorreto.")