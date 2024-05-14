from Komponenter import Komponenter


class Hovedkort(Komponenter):
    def __init__(self, modell, produsent, garanti, verdi, formfaktor, prosessor_sokkel):
        super().__init__(modell, produsent, garanti, verdi)
        self.formfaktor = formfaktor
        self.prosessor_sokkel = prosessor_sokkel

    def vis_data(self):
        super().vis_data()
        print(f"Formfaktor: {self.formfaktor}")
        print(f"Prosessorsokkel: {self.prosessor_sokkel}")



