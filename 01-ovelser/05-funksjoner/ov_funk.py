# Definisjonen av funksjonen
def hei():
    print("Hei på deg!")

# Kallet til funksjonen
#hei()

# Funksjon for å beregne areal på rektangel

lengde = 10
bredde = 5

#Areal rektangel
def areal_rek(l,b):
    A = l * b
    return A

print(areal_rek(lengde,bredde))


radius = 6
# A = pi * radius ** 2

#Areal sirkel
def areal_sirk(r):
    A = 3.14 * r**2
    return A

print(areal_sirk(radius))
