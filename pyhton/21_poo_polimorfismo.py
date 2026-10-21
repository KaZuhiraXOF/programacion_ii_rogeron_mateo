class Guerrero:
    nombre : str
    poder_inicial : int
    horas : int

    def __init__(self, nombre : str, poder_inicial : int, horas : int):
        self.nombre = nombre
        self.poder_inicial = poder_inicial
        self.horas = horas  
    def atacar(self):
        print(f"{self.nombre} realiza un ataque")

    def calcular_poder(self):
        return self.poder_inicial

class Goku(Guerrero):
    def __init__(self, nombre : str, poder_inicial : int, horas : int):
        super().__init__(nombre, poder_inicial, horas)

    def atacar(self):
        print(f"{self.nombre} utiliza kamehameha")

    def calcular_poder(self):
        return self.poder_inicial + self.horas * 100

class Vegeta(Guerrero):
    def __init__(self, nombre : str, poder_inicial : int, horas : int):
        super().__init__(nombre, poder_inicial, horas)

    def atacar(self):
        print(f"{self.nombre} utiliza final flash")

    def calcular_poder(self):
            return self.poder_inicial + self.horas * 150

goku = Goku("Gran Goku", 150, 50)
vegeta = Vegeta("Príncipe Vegeta", 200, 80)
goku.atacar()
vegeta.atacar()
print(vegeta.calcular_poder())
print(goku.calcular_poder())
