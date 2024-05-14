# verdier til et A4 ark
# 21cm / 210mm bredde
A4bredde = float(input("Velg bredden til arket: ")) #21
# 29.7cm / 297mm høyde/lengde
A4lengde = float(input("Velg lengden til arket: ")) #29.7

# funksjon for beregning av volum. Tar høyde som innverdi
def volumRegning(h):
    #grunn flate = lengde x bredde
    g = (A4lengde - h * 2) * (A4bredde - h * 2)
    #volum = grunnflate x hoyde
    V = g * h
    return V


# hoyde for eksen
hoyde = 0.000001

#inkrementell vekst variabel
inkrement = 0.01

#while løkke for volum regningen med inkrement til utfallet er optimalisert
while volumRegning(hoyde) < volumRegning(hoyde + inkrement):
    #hoyde adderes med inkrement
    hoyde += inkrement
    #hver høyde printes til den er optimalisert
    print(hoyde)

# Optimalisert volum printes
print("Svar volum:",volumRegning(hoyde))