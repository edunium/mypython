"""
crear un programa que agregue alentos en una lista menor a 120 y mostrar los elemtos

"""

lista_elementos = []

for x in range(0, 13):
    lista_elementos.append(f"\nelemento {x}")
    print(x)

print(lista_elementos)
    
    
contador = 0

while contador <= 12:
    lista_elementos.append(f"\nelemento {contador}")
    print(contador)
    contador += 1

print(lista_elementos)
