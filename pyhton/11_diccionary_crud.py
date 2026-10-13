droides = [
    {
        "codigo": "B1-001",
        "modelo": "B1",
        "energia": 90,
        "activo": True
    },
    {
        "codigo": "B1-002",
        "modelo": "B1",
        "energia": 40,
        "activo": False
    },
    {
        "codigo": "B1-003",
        "modelo": "Droideka",
        "energia": 80,
        "activo": True
    }
]

#CREATE
cantidad_droides = len(droides)
print(cantidad_droides)

nuevo_droide = {
    "codigo": "B1-004",
    "modelo": "B1",
    "energia": 100,
    "activo": True
}
droides.append(nuevo_droide)
print(len(droides))

#READ
droide = droides[2]
print(f"Codigo: {droide["codigo"]}")
print(f"Modelo: {droide["modelo"]}")
print(f"Energia: {droide["energia"]}")
print(f"Activo: {droide["activo"]}")

#UPDATE

droide = droides[2]
droide["codigo"] = "DRO-002"
droide["energia"] = 85
droide["activo"] = False
print(f"Droide: {droides[2]}")

#DELETE

eliminado = droides.pop(2)
print(f"Droide: {droides}")