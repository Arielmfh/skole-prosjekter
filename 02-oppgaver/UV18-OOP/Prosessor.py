from Komponenter import Komponenter

class Prosessor(Komponenter):
    def __init__(self, modell, produsent, garanti, verdi, antall_kjerner, klokkefrekvens):
        super().__init__(modell, produsent, garanti, verdi)
        self.antall_kjerner = antall_kjerner
        self.klokkefrekvens = klokkefrekvens

    def vis_data(self):
        super().vis_data()
        print(f"Antall kjerner: {self.antall_kjerner}")
        print(f"Klokkefrekvens: {self.klokkefrekvens}")



