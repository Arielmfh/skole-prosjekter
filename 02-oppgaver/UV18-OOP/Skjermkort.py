#Importerer komponent superklasse

from Komponenter import Komponenter

# Definerer skjermprosessor subklasse

class Skjermkort(Komponenter):
    def __init__(self, modell, produsent, garanti, verdi, maks_skjermer, maks_opplosning, ant_cuda_kjerner, videominne):
        super().__init__(modell, produsent, garanti, verdi)
        self.maks_skjermer = maks_skjermer
        self.maks_opplosning = maks_opplosning
        self.ant_cuda_kjerner = ant_cuda_kjerner
        self.videominne = videominne

    def vis_data(self):
        super().vis_data()
        print(f"Maks skjermer: {self.maks_skjermer}")
        print(f"Maks oppløsning: {self.maks_opplosning}")
        print(f"Antall CUDA kjerner: {self.ant_cuda_kjerner}")
        print(f"Videominne: {self.videominne}")


