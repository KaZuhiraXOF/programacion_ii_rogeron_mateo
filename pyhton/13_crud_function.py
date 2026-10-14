flota = [
    {
        "N1-001": {
            "nombre": "Caza N-1"
        }
    },
    {
        "NR-002": {
            "nombre": "Nave Real",
            "combustible": 80
        }
    }
]

def crear_nave(nave):
    flota.append(nave)

def update_nave(index, nave_upd):
    flota[index].update(nave_upd)

def borrar_nave(index):
    return flota.pop(index)

def leer_nave(index):
    return flota[index]

print("1:", flota)

nueva_nave = {
    "NR-003": {
        "nombre": "Nave Real 2",
        "combustible": 85
    }
}

crear_nave(nueva_nave)
print("2:", flota)

nueva_update = {
    "NR-003": {
        "nombre": "Nave Real Modificada",
        "combustible": 90
    }
}

update_nave(2, nueva_update)
print("3:", flota)

print("4:", leer_nave(2))
print("5:", borrar_nave(2))
print("6:", flota)