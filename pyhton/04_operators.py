#Operadores

'''
OPeradores aritméticos
+ Suma
- Resta
* Multiplicación
/ División
% Módulo
** Exponente
// División entera
'''

valor1 = 7
valor2 = 3

suma = valor1 + valor2
resta = valor1 - valor2
multiplicacion = valor1 * valor2
division = valor1 / valor2
modulo = valor1 % valor2
exponente = valor1 ** valor2
division_entera = valor1 // valor2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Módulo:", modulo)
print("Exponente:", exponente)
print("División entera:", division_entera)

print("Tabla de multiplicar del 5")
multi = 5
print(f"{multi} * 1 = {multi*1}")
print(f"{multi} * 2 = {multi*2}")
print(f"{multi} * 3 = {multi*3}")
print(f"{multi} * 4 = {multi*4}")
print(f"{multi} * 5 = {multi*5}")
print(f"{multi} * 6 = {multi*6}")
print(f"{multi} * 7 = {multi*7}")
print(f"{multi} * 8 = {multi*8}")
print(f"{multi} * 9 = {multi*9}")
print(f"{multi} * 10 = {multi*10}")

print("Area de un triangulo con base 5 y altura 10: ", (5*10)/2)

#for i in range(1,11):
#    print(f"5 muliplicado por {i} es igual a {5*i}")

'''
Operadores de comparación
== Igual a
!= Diferente de
> Mayor que
< Menor que
>= Mayor o igual que
<= Menor o igual que
'''

velocidad_anakin = 950
velocidad_sebulba = 900

print("Anakin es más rápido que Sebulba?: ", velocidad_anakin > velocidad_sebulba)
print("Anakin es más lento que Sebulba?: ", velocidad_anakin < velocidad_sebulba)
print("Anakin es igual de rápido que Sebulba?: ", velocidad_anakin == velocidad_sebulba)
print("Anakin es diferente de Sebulba?: ", velocidad_anakin != velocidad_sebulba)
print("Anakin es más rápido o igual que Sebulba?: ", velocidad_anakin >= velocidad_sebulba)
print("Anakin es más lento o igual que Sebulba?: ", velocidad_anakin <= velocidad_sebulba)

resultado = velocidad_anakin > velocidad_sebulba
print("Resultado de la comparación:", resultado)
print("Tipo de dato del resultado:", type(resultado))

'''
Operdores lógicos
and: Devuelve True si ambos operandos son True
or: Devuelve True si al menos uno de los operandos es True
not: Devuelve True si el operando es False, y viceversa
'''

motores_funcionales = True
Escudo_funcional = False
combustible = 80

print("Todos los sistemas están funcionando?: ", motores_funcionales and Escudo_funcional)
print("Al menos un sistema está funcionando?: ", motores_funcionales or Escudo_funcional)
print("Los motores no están funcionando?: ", not motores_funcionales)


cantidad_motores = 2
cantidad_alas = 4
combustible = 80

print("La nave tiene 2 motores y 4 alas?: ", cantidad_motores == 2 and cantidad_alas == 4)
print("La nave tiene al menos 2 motores o 4 alas?: ", cantidad_motores >= 2 or cantidad_alas >= 4)
print("La nave no tiene 2 motores?: ", not cantidad_motores == 2)

'''
Operadores de asignación
= Asignación
+= Suma y asignación
-= Resta y asignación
*= Multiplicación y asignación
/= División y asignación
%= Módulo y asignación
**= Exponente y asignación
//= División entera y asignación
'''

velocidad = 100
print("Velocidad inicial:", velocidad)
velocidad += 50
print("Velocidad después de acelerar:", velocidad)
velocidad -= 30
print("Velocidad después de frenar:", velocidad)
multiplicador = 2
velocidad *= multiplicador
print("Velocidad después de multiplicar por 2:", velocidad)
divisor = 4
velocidad /= divisor
print("Velocidad después de dividir entre 4:", velocidad)
modulo = 7
velocidad %= modulo
print("Velocidad después de aplicar módulo 7:", velocidad)
velocidad **= 3
print("Velocidad después de elevar al cubo:", velocidad)


'''
Precedencia de operadores
1. Paréntesis ()
2. Exponente **
3. Multiplicación *, División /, Módulo %
4. Suma +, Resta -
5. Comparación ==, !=, >, <, >=, <=
6. Lógicos and, or, not
'''

resultado_1 = 10 + 5 * 2
print("Resultado: ", resultado_1)
resultado_2 = (10 + 5) * 2
print("Resultado: ", resultado_2)
resultado_3 = 10 + 5 * 2 **2
print("Resultado: ", resultado_3)
