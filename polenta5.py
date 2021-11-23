"""

crear 4 variables lista, string, entera y booleana e imprimir su tipo
usar funciones


"""

def traducir(tipo):
    result = None
    if tipo == list:
        result = "lista"
    elif tipo == str:
        result = "cadena"
    elif tipo == int:
        result == "entero"
    elif tipo == bool:
        result == "booleana"
    
    return result
        
        


def comprobar(dato, tipo):
    
    test = isinstance(dato, tipo)
    result = ""
    if test:
        result = f"este dato es de tipo {traducir(tipo)}"
    else:
        result = "el tipo de dato no es corresto"
    return result

var_lista = ["hola mundo, 77"]
var_texto = "eduardo herrera"
var_numero = 48
var_booleana = True

print(comprobar(var_lista, list))
print(comprobar(var_texto, str))
print(comprobar(var_numero, int))
print(comprobar(var_booleana, bool))

