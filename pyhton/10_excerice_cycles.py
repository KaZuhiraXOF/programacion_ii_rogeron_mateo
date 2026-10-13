'''
Control de flotas
'''

naves = [
    {
        "nombre": "Caza N-1",
        "combustible": 80,
        "droides": ["R2-D2","R2-A6"]
    },
    {
        "nombre": "Caza Real",
        "combustible": 35,
        "droides": ["R2-N3"]
    },
    {
        "nombre": "Transporte",
        "combustible": 65,
        "droides": ["R2-D2","R2-A6"]
    },
]

nave_lista = 0
naves_recarga = 0
total_droides = 0
total_ciclos = 0

for numero,nave in enumerate(naves, start=1):
    print(f"=== NAVE : {numero} - {nave}")
    if nave["combustible"] >= 50:
        print(f"Estado inicial: LISTA")
        nave_lista += 1
    else:
        print(f"Estado inicial: RECARGA")
        naves_recarga += 1
        ciclo = 0
        while nave["combustible"] <= 50:
            ciclo += 1
            nave["combustible"] += 10
        total_ciclos += ciclo
        print("Recarga completada")
        print("Estado final: LISTA")

    total_droides += len(nave["droides"])

    for droide in nave["droides"]:
        print(f"Droide: {droide}")

print("==============================")
print("========R E S U M E N=========")
print("==============================")

print(f"Total de naves: {len(naves)}")
print(f"Naves listas inicial: {nave_lista}")
print(f"Naves recargadas: {naves_recarga}")
print(f"Total Droides: {total_droides}")
print(f"Total Ciclos de recarga: {total_ciclos}")
