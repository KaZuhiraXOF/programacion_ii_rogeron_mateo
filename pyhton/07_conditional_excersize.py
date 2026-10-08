costo_envio = 0

peso_paquete = float(input("Ingresa el peso del paquete: "))

print("Cuál es la zona de envío?")
print("1: América")
print("2: Europa")
print("3: Resto del mundo")

num1 = int(input())

if num1 < 1 or num1 > 3:
    print("Error, la zona de envío es inexistente... Calculo cancelado")
elif num1 == 3:
    print("El costo de envío del paquete es de: ", peso_paquete * 10), "$"
elif num1==2:
    print("El costo de envío del paquete es de: ", peso_paquete * 7.5, "$")
elif num1==1:
    print("El costo de envío del paquete es de: ", peso_paquete * 5, "$")
  