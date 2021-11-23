# lista de 8 numeros
# hacer...recorrer lista y mostrar
# ordenar y mostrar
# mostrar su longitud
# buscar algun elemento (pedir por teclado



lista_numeros = [13, 25, 26, 48, 2, 5, 9, 10]
contador = len(lista_numeros)

print("\n++++++++++++RECORRE Y MUESTRA LISTA+++++++++++++")

for x in range(0, contador):
    print(f"elemento de la lista: {lista_numeros[x]}")

print("\n++++++++++++LISTA ORDENADA+++++++++++++")

lista_numeros.sort()

for y in range(0, contador):
    print(f"elemento de la lista: {lista_numeros[y]}")

print("\n++++++++++++LONGITUD LISTA+++++++++++++")

contador = len(lista_numeros)
print(f"longitud de la lista es: {contador}")    

def ver_elemento(elemento):
    print(f"elemento ingresado es: {lista_numeros[elemento]}")
 
elemento = int(input("ingrese un numero de la lista a buscar "))
elemento = elemento - 1
ver_elemento(elemento)

lista_numeros.sort()
print(lista_numeros)
