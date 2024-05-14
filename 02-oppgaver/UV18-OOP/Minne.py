from Komponenter import Komponenter

class Minne(Komponenter):
    def __init__(self, modell, produsent, garanti, verdi, minnetype, minnestørrelse, hastighet):
        super().__init__(modell, produsent, garanti, verdi)
        self.minnetype = minnetype
        self.minnestørrelse = minnestørrelse
        self.hastighet = hastighet

    def vis_data(self):
        super().vis_data()
        print(f"Type minne: {self.minnetype}")
        print(f"Størrelse: {self.minnestørrelse}")
        print(f"Hastighet: {self.hastighet}")


