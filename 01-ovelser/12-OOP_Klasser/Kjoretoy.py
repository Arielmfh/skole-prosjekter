    # Definere klassen Kjoretoy

class Kjoretoy:
    def __init__(self, merke, aarsmodell, farge):
        self.merke = merke
        self.aarsmodell = aarsmodell
        self.farge = farge

    def vis_data(self):
        print("Merker:",self.merke)
        print("Årsmodell:",self.aarsmodell)
        print("Farge:",self.farge)

    def sett_farge(self,farge):
        self.farge = farge
        

mc1 = Kjoretoy("Honda", 2021, "Rød")


mc1.vis_data()

mc1.sett_farge("Grå")

mc1.vis_data()