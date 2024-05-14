# Alle areal funksjoner

# Funksjon for å beregne kvadrat
def areal_kvdt(s):
    A = s ** 2
    return A

# Funksjon for å beregne areal på rektangel

#Areal rektangel
def areal_rek(l,b):
    A = l * b
    return A


# Funksjon for å beregne arealet til en trekant

def areal_trekt(g,h):
    A = g * h / 2
    return A


# Funksjon for å beregne arealet til en parallellogram

def areal_pllg(g,h):
    A = g * h
    return A

#Funksjon for å beregne areal til en rombe

def areal_rombe(g,h):
    A = g * h
    return A
# (1 / 2) * (base1 + base2) * height

#Funksjon for å beregne areal til en trapes

def areal_trap(a,b,h):
    A = (a + b) * h / 2 # (1 / 2) 
    return A

#Funksjon for å beregne areal på sirkel

def areal_sirk(r):
    A = 3.14 * r**2
    return A



######## Kall til funksjoner ########
print("Tilgjengelige funksjoner for beregning av Areal:")

print("Kvadrat, Rektangel, Trekant, Parallellogram, Rombe, Trapes, Sirkel")

print("Velg en av listen over, skriv med stor forbokstav!")

velgFunksjon = input("Hvilken funksjon vil du bruke? ")

# mellomrom
print(" ")

if velgFunksjon == "Kvadrat":
    print("Arealet til en kvadrat er side opphøyd i 2")
    side = int(input("Hvilket verdi har siden til kvadraten? "))
    print("Arealet til kvadraten er",areal_kvdt(side))
elif velgFunksjon == 'Rektangel':
    print('Arealet til et rektangel er lengde x bredde')
    lengde = int(input("Hvilken verdi har lengden til rektangelen? "))
    bredde = int(input("Hvilken verdi har bredde til rektangelen? "))
    print("Arealet til rektangelen er",areal_rek(lengde,bredde))
elif velgFunksjon == "Trekant":
    print ("Arealet til en trekant er grunnlinjen x høyden delt på 2")
    gVerdi = int(input("Hvilken verdi har grunnlinjen til trekanten? "))
    hoyd = int(input("Hvilken verdi har høyden til trekanten? "))
    print("Arealet til trekanten er",areal_trekt(gVerdi,hoyd))
elif velgFunksjon == "Parallellogram":
    print("Arealet til et parallellogram er grunnlinje x høyde")
    grunnLinje = int(input("Hvilken verdi har grunnlinjen til parallellogrammen? "))
    hoydeP = int(input("Hvilken verdi har høyden til parallellogrammen? "))
    print("Arealet til parallellogrammen er",areal_pllg(grunnLinje,hoydeP))
elif velgFunksjon == "Rombe":
    print("Arealet til en Rombe er grunnlinje x høyde")
    gLinje = int(input("Hvilken verdi har grunnlinjen til parallellogrammen? "))
    hoydeR = int(input("Hvilken verdi har høyden til parallellogrammen? "))
    print("Arealet til parallellogrammen er",areal_pllg(gLinje,hoydeR))   
elif velgFunksjon == "Trapes":
    print("Arealet til en Trapes er lengden av de to parallelle siden x høyden delt på 2") 
    base1 = int(input("Hva er verdien til bunnen av trapesen? (Første parallelle linje) "))   
    base2 = int(input("Hva er verdien til toppen av trapesen? (Andre parallelle linje) "))
    hoydeTr = int(input("Hva er høyden til trapesen? "))  
    print("Arealet til en Trapes er",areal_trap(base1,base2,hoydeTr))
elif velgFunksjon == "Sirkel":
    print("Arealet til en sirkel er pi x radius opphøyd i 2")
    Radius = int(input("Skriv inn radien til sirkelen: "))  
    print("Arealet til sirklene er",areal_sirk(Radius))
else:
    print("Sjekk stavingen din!")

