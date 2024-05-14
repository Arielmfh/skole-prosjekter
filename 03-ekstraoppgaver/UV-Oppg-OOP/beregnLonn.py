# Importerer nodvendige biblioteker
import random


# Person super class
class Person:
    def __init__(self, fornavn, etternavn, id, timelonn):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.id = id
        self.timelonn = timelonn

    # Metoder
    def EndreLonn(self, ny_timelonn):
        print(f"{self.fornavn} gammel timelønn: {self.timelonn}")
        self.timelonn = ny_timelonn
        print(f"{self.fornavn} ny timelønn: {self.timelonn}")

    def EndreTimeLonn(self):
        gammel = self.timelonn
        ny = int(input("Ansatt ny timelonn: "))
        self.timelonn = ny
        print(f"Gammel timelønn: {gammel}")
        print(f"Ny timelonn: {self.timelonn}")

    def SkrivUt(self):
        print("-------------------------------")
        print(f"Ansatt fornavn: {self.fornavn}")
        print(f"Ansatt etternavn: {self.etternavn}")
        print(f"{self.fornavn} ID: {self.id}")
        print(f"Timelønn: {self.timelonn}")


# Ansatt class
class Ansatt(Person):
    def __init__(self, fornavn, etternavn, id, timelonn, antall_timer):
        super().__init__(fornavn, etternavn, id, timelonn)
        self.antall_timer = antall_timer

    def beregn_lonn(self, antall_timer):
        lonn = self.antall_timer * self.timelonn
        print(f"{self.fornavn} sin lønn er {lonn} med {antall_timer}t arbeid")

    def id_navn(self):
        print(f"{self.fornavn}")


# Leder class


class Leder(Person):
    def __init__(self, fornavn, etternavn, id, timelonn, antall_timer, bonus):
        super().__init__(fornavn, etternavn, id, timelonn)
        self.antall_timer = antall_timer
        self.bonus = bonus

    def beregn_lonn(self):
        print("----------------------------------")
        self.bonus = random.randint(13, 19)
        print(f"Leder bonus: {self.bonus}%")
        lonn = (self.antall_timer * self.timelonn) * self.bonus
        print(f"Leder lønn for {self.antall_timer}t arbeid er {lonn}kr med en timelønn på {self.timelonn}")

    def SkrivUt(self):
        print("----------------------------------")
        print(f"Leder fornavn: {self.fornavn}")
        print(f"Leder etternavn: {self.etternavn}")
        print(f"Leder ID: {self.id}")
        print(f"Leder timelønn: {self.timelonn}")

    def id_navn(self):
        print(f"{self.fornavn}")


test1 = Ansatt("Ariel", "Heggernes", 1, 135, 35)
test1.beregn_lonn(35)
test1.EndreLonn(147)
test1.beregn_lonn(35)
test1.SkrivUt()


leder1 = Leder("Edgar", "Fernandez", 2, 235, 24, 13)
leder1.SkrivUt()
leder1.beregn_lonn()

print("1: Endre timelønn, 2: Exit")
modus = input("Modus? ")

if modus == "1":
    print("Tilgjengelige ansatte og ledere:")
    test1.id_navn()
    leder1.id_navn()
    hvilken_ansatt = input("Ansatt hvilken fornavn? ")
    if hvilken_ansatt == "Ariel":
        print("----")
        test1.EndreTimeLonn()
        print("----")
        test1.beregn_lonn(24)
        print("----")
        mer_info = input("Se ansatt info? Ja/Nei: ")
        if mer_info == "Ja" or mer_info == "ja":
            test1.SkrivUt()
        elif mer_info == "Nei" or mer_info == "nei":
            exit()
        else:
            exit()
    elif hvilken_ansatt == "Edgar":
        leder1.EndreTimeLonn()
        leder1.beregn_lonn()
        mer_info = input("Se ansatt info? Ja/Nei: ")
        if mer_info == "Ja" or mer_info == "ja":
            leder1.SkrivUt()
        elif mer_info == "Nei" or mer_info == "nei":
            exit()
        else:
            exit()
elif modus == "2":
    exit()

