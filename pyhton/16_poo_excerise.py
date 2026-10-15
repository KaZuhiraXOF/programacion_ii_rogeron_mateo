class RadarDragon:
	region1: int
	region2: int
	
	def __init__(self, region1: int, region2: int):
		self.region1 = region1
		self.region2 = region2

	def buscar_esferas(self):
		esfe_enco = self.region1 + self.region2
		print("Esferas del dragon encontradas:", esfe_enco)
		if esfe_enco < 7:
			print(f"Para invocar a Shen Long hace falta {7 - esfe_enco}")
		elif esfe_enco == 7:
			print("Es hora de invocar a shen long")

radar_bulma = RadarDragon(3,2)

radar_bulma.buscar_esferas()
