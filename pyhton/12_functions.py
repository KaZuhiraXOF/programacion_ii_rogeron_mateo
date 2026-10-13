def activar_sistema():
    print("==Sisteme Naboo")
    print("Sistema de control activado")

def saludar_jedi(nombre):
    print(f"Que la fuerza te acompañe: {nombre}")

def mostrar_nave(nombre, combustible):
    print(f"nave: {nombre}")
    print(f"cantidad de combustible: {combustible}")

#funciones que devuelven dato o informacion
def calcular_combustible(inicial, consumo):
    restante = inicial - consumo
    return restante



activar_sistema()
saludar_jedi("Qui-gon Jinn")
saludar_jedi("Obi-Wan Kenobi")
mostrar_nave("Caza N-1",80)
resultado = calcular_combustible(85,63)
print(f"Combustible: {resultado}")
