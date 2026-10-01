import os
os.system("cls")

area1 = int(input("medida 1"))
area2 = int(input("medida 2"))
area3 = int(input("medida 3"))

if area1 < 0 and area2 < 0 and area3 <0:
    print("area invalida")

elif area1 == area2 and area1 == area3:
    print("Triangulo euqilatero")

elif area1 == area3 or area1 == area2:
    print("Triangulo isocelis")

else:
    print("Triangulo escaleno")