# BEHANDLING AV LISTER(ARRAYS) i PYTHON

# Opprett en liste med elementer
min_liste = ["Petter","Hanne","Kåre","Thor"]


# Skriv ut en liste
print(min_liste)


# Kontroller at det er en liste
print(type(min_liste))


# Hvor mange elementer inneholder en liste
print("Antall elementer: ",len(min_liste))


# Opprett en tom liste
min_liste_2 = []


# Legg til et element i en liste
min_liste.append("Kari")
print(min_liste)


# Tillatt med duplikate verdier i liste
min_liste.append("Hanne")
print(min_liste)


# les et element i en liste. Fra starten og fra enden. 
print(min_liste[0])
navn = min_liste[1]
print(min_liste[-1])


# Endre et element i en liste
min_liste[3] = "Tor"


# Sett inn et element i en liste
min_liste.insert(1,"Jonas")
print(min_liste)


# Slett element i liste
min_liste.remove("Hanne")
min_liste.pop(0)
print(min_liste)


# En tekststreng (string) er en liste. OBS! Du kan ikke kjøre append på en string.
min_tekst = "Ariel"
#print(min_tekst[2])


# Løkker og lister
for i in range(len(min_tekst)):
    print(min_tekst[i])
