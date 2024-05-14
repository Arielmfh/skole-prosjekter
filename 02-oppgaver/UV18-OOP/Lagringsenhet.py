from Komponenter import Komponenter

class Lagringsenhet(Komponenter):
    def __init__(self, modell, produsent, garanti, verdi, lagringstype, kapasitet):
        super().__init__(modell, produsent, garanti, verdi)
        self.lagringstype = lagringstype
        self.kapasitet = kapasitet

    def vis_data(self):
        super().vis_data()
        print(f"Lagringstype: {self.lagringstype}")
        print(f"Kapasitet: {self.kapasitet}")


# Testdata for Lagringsenhet
storage1 = Lagringsenhet("Samsung 970 EVO", "Samsung", "5 år", "1 500 kr", "SSD", "1 TB")
storage2 = Lagringsenhet("Western Digital Blue", "WD", "3 år", "800 kr", "HDD", "1 TB")
