from Komponenter import Komponenter

class Stromforsyning(Komponenter):
    def __init__(self, modell, produsent, garanti, verdi, watt, effektivitet, modularitet):
        super().__init__(modell, produsent, garanti, verdi)
        self.watt = watt
        self.effektivitet = effektivitet
        self.modularitiet = modularitet

    def vis_data(self):
        super().vis_data()
        print(f"Watt: {self.watt}")
        print(f"80 Plus Sertifisering: {self.effektivitet}")
        print(f"\nModularity: {self.modularitiet}")


# Testdata for Strømforsyning
psu1 = Stromforsyning("Corsair RM750", "Corsair", "3 år", "1 200 kr", 750, "80 Plus Gold", "Modular")
psu2 = Stromforsyning("EVGA 600 BQ", "EVGA", "3 år", "600 kr", 600, "80 Plus Bronze", "Non-modular")
