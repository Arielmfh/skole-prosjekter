# Importerer klassen kjoretoy
from Kjoretoy import Kjoretoy

# Definere klassen MC

class Mc(Kjoretoy):
    def __init__(self, merke, aarsmodell, farge, drivverk):
        super().__init__(merke, aarsmodell, farge)
        self.drivverk = drivverk

    def vis_data(self):
        super().vis_data()
        print("Drivverk:",self.drivverk)