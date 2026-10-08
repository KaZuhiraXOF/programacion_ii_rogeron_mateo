#Condicional if
#Simple

combustible = 10
if combustible >= 10:
    print("Puede despegar")

#Condicional if-else

creditos = int(input("Ingrese la cantidad de creditos que tienes: "))
precio_respuesto = int(input("Ingrese el precio del repuesto: "))
if creditos >= precio_respuesto:
    print("Puede comprar el repuesto")
else:
    print("No tienes suficientes creditos para comprar el repuesto")

#if anidado

if creditos >= precio_respuesto:
    print("Puede comprar el repuesto")
    if creditos > precio_respuesto:
        print("Le sobran creditos")
    else:
        print("No le sobran creditos")
else:
    print("No tienes suficientes creditos para comprar el repuesto")

#condicional if-elif-else

if creditos > precio_respuesto:
    print("Puede comprar el repuesto y le sobran creditos")
elif creditos == precio_respuesto:
    print("Puede comprar el repuesto pero no le sobran creditos")
else:
    print("No tienes suficientes creditos para comprar el repuesto")


tipo_repuesto = input("Ingrese el tipo de repuesto (motor, ala o escudo): ")
if tipo_repuesto == "motor" and creditos >= precio_respuesto and tipo_repuesto != "ala" and tipo_repuesto != "escudo":
    print("Puedes comprar el respueso y te sobran creditos")
elif tipo_repuesto == "ala" and creditos >= precio_respuesto and tipo_repuesto != "motor" and tipo_repuesto != "escudo":
    print("El repuesto es un ala")
elif tipo_repuesto == "escudo" and creditos >= precio_respuesto and tipo_repuesto != "motor" and tipo_repuesto != "ala":
    print("El repuesto es un escudo")
else:
    print("Tipo de repuesto no válido")


