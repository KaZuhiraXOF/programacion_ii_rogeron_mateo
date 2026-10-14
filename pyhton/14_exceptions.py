print("=====CONTROL DE ENERGÍA=====")
energia_texto = "ochenta"
try:
    energia=int(energia_texto)
    print(energia)
    '''si se especifica el valor solo hara el valor, acaso contrario ir por todo los errores'''
except ValueError:
    print("ERROR DETECTADO: debe ser un dato numérico")

print ("Fin del sistema")

'''
ValueError
TypeError
IndexError
KeyError
ZeroDivisionError
'''

def calcular_energia(total, cantidad):
    try:
        resultado = total/cantidad
        return resultado
    except ZeroDivisionError:
        print("Error: division entre cero")
        return None
    except TypeError:
        print("Error: valores deben ser numericos")
        return None

print("Caso 1: ", calcular_energia(100,4))
print("Caso 2: ", calcular_energia(100,0))
print("Caso 3: ", calcular_energia(100,"cuatro"))

print("=======DIAGNÓSTICO R2-D2=========")
try:
    energia = int("cuatro")
    print("energia: ", energia)
except ValueError:
    print("Error de lectura")
else:
    print("diagnostico completado")
finally:
    print("Cerrando diagnóstico")


##########################


def validar_energia(energia):
    if type(energia) is not int:
        raise TypeError("La energía debe ser número entero")
    elif energia < 0 or energia >100:
        raise ValueError("La energia debe estar entre 0 y 100")
    return energia

try:
    resultado = validar_energia(60)
    print("Energia: ", resultado)
except(TypeError, ValueError) as error:
    print(f"Error: {error}")