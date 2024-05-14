# Importerer fra kjoretoy
from Kjoretoy import Kjoretoy

# Definerer klasse Buss

class Buss(Kjoretoy):
    def __init__(self, merke, aarsmodell, farge, ant_seter):
        super().__init__(merke, aarsmodell, farge)
        self.ant_seter = ant_seter

    def vis_data(self):
        super().vis_data()
        print("Antall seter:",self.ant_seter)