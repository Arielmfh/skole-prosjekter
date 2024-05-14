# Definerer superklassen til komponenter


class Komponenter:
    def __init__(self, modell, produsent, garanti, verdi):
        self.modell = modell
        self.produsent = produsent
        self.garanti = garanti
        self.verdi = verdi

    def vis_data(self):
        print("-----------------------------")
        print("Modell:", self.modell)
        print("Produsent:", self.produsent)
        print("Garanti:", self.garanti)
        print("Verdi:", self.verdi)


