# importerer random
import random

#variabel for minimum tilfeldig tall
minimum = 1
#variabel for maksimum tilfeldig tall
maksimum = 2

# input for brukeren sin gjettet tall
bruker_tall = int(input("Gjett et tall mellom 1 til 10: "))

# variabel for antall gjett
antall_gjett = 1

# tilfeldig tall mellom 1 til 10 velges
t_tall = random.randint(minimum,maksimum)

# true-false variabel for om brukeren har gjettet riktig 
riktig = False

# løkke som sjekker om true-false variabelen er sann eller usann for å kjøre forekommende if-setninger. Hvis den er usann kjøres if-setningene
while riktig == False:
    # brukeren sitt tall blir sjekket med det tilfeldige tallet
# if bruker_tall > t_tall:
  if bruker_tall > t_tall:
    #print("Tallet ditt var for høyt")
    print("Tallet ditt var for høyt")
    #input brukeren for å gjette på nytt
    bruker_tall = int(input("Gjett et tall mellom 1 til 10: "))
    # antall gjett inkrementeres med 1
    antall_gjett += 1
# elif bruker_tall < t_tall:
  elif bruker_tall < t_tall:
    #print("Tallet ditt var for lavt")
    print("Tallet ditt var for lavt")
    #input brukeren for å gjette på nytt
    bruker_tall = int(input("Gjett et tall mellom 1 til 10: "))
    # antall gjett inkrementeres med 1
    antall_gjett += 1
# elifif bruker_tall == t_tall:    
  elif bruker_tall == t_tall:
    #print("Gjettet ditt var riktig! Du har vunnet")
    print("Gjettet ditt var riktig! Du har vunnet")
    # Brukeren for vite hvor mange forsøk de brukte
    print("Du gjettet",antall_gjett,"ganger!")
    #true-false variabel for spillet blir satt til riktig
    riktig = True 