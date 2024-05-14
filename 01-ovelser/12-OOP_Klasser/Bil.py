# Importerer fra Kjoretoy
from Kjoretoy import Kjoretoy
# Definere klassen Bil

class Bil:
    def __init__(self, merke, aarsmodell, farge, ant_dorer):
        super().__init__(merke, aarsmodell, farge)
        self.ant_dorer = ant_dorer

    def vis_data(self):
        super().vis_data
        print("Antall dører:",self.ant_dorer)