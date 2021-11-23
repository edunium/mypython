"""

verificar una variable si esta vacia o no... si esta vacia agregar tecto en minisculas y mostrar


"""

entrada = input("ingrese un texto:")

if len(entrada.strip()) <= 0:
    entrada = "se va a rellenar entrada"
    print(entrada.upper())

else:
    print(f"la variable tiene contenido {entrada}")
