import importlib

mod = importlib.import_module("19_poo_guerrero")
Guerrero = mod.Guerrero

class Saiyajin(Guerrero):
    def __init__(self, nombre:str):
        super().__init__(nombre)

    def transformarse(self):
        print(f"{self.nombre} alcanzò la forma del Super SaiyajiSSSn")