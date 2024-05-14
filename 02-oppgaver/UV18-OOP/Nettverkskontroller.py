from Komponenter import Komponenter

class Nettverkskontroller(Komponenter):
    def __init__(self, modell, produsent, garanti, verdi, nettverkstype, hastighet):
        super().__init__(modell, produsent, garanti, verdi)
        self.nettverkstype = nettverkstype
        self.hastighet = hastighet

    def vis_data(self):
        super().vis_data()
        print(f"Nettverkstype: {self.nettverkstype}")
        print(f"Hastighet: {self.hastighet}")



