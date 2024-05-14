from Komponenter import Komponenter

class Kjolingsenhet(Komponenter):
    def __init__(self, modell, produsent, garanti, verdi, kjølemetode):
        super().__init__(modell, produsent, garanti, verdi)
        self.kjolemetode = kjølemetode

    def vis_data(self):
        super().vis_data()
        print(f"Kjølemetode: {self.kjolemetode}")



