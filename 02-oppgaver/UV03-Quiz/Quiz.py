# Variabel for antall riktige svar
riktige_svar = 0

# Variabel for spørsmål streng
bruker_sporsmal = ""
# Variabel for antall spørsmål svart
sporsmal_svart = 0

# Spørsmål som variabler
sporsmol_1 = "Hvilket klasserom er vi i? Svar: "
sporsmol_2 = "Hva er første bokstaven i alfabetet? Svar: "
sporsmol_3 = "Hva er den siste bokstaven i det norske alfabetet? Svar: "
sporsmol_4 = "Hvilket bokstav begynner dyret med? Hjort eller gjort. Svar: "
sporsmol_5 = "Skriv inn den manglende bokstaven på fotball-laget; AC _ilan Svar: "
sporsmol_6 = "(s)ant eller (u)sant, Donald Ducks tre nevøer heter Ole, Dole og Daffen? Svar: "
sporsmol_7 = "Er Romeo og Julie basert på en ekte historie? (j)a eller (n)ei? Svar: "
sporsmol_8 = "Hvor er hunderasen, Chihuahaen fra? (n)ord amerika eller (a)sia? Svar: "
sporsmol_9 = "(s)ant eller (u)sant, det er ca. 2700 forskjellige språk i verden. Svar: "
sporsmol_10 = "(s)ant eller (u)sant, IT står for Internet Technology? Svar: "

# Print med kort info om Quizen. Det svares kun med småe bokstaver
print("NB! Svar kun med småe bokstaver på quizen. Hvert svar har kun ett bokstav. Lykke til!")

# If-setning som sjekker innholdet til spørsmål svar variabelen 
# Antall spørsmål svart sjekkes og da blir du stilt neste spørsmål i rekkefølge. Det printes hvilket spørsmål brukeren er i
if sporsmal_svart == 0:    
  print(" SPØRSMÅL 1 ")
  bruker_sporsmal = input(sporsmol_1)
else:
  print("Noe gikk feil. Vennligst start på nytt")

# If setning som sjekker om bruker input er riktig besvarelse
if bruker_sporsmal == "b":
    # Hvis bruker har svart riktig får han +1 i antall riktige svar og det printes at de har svart riktig
    riktige_svar += 1
    print("Riktig! Fortsett sånn")
    # Antall spørsmål svart variabelen bestiges med én
    sporsmal_svart += 1
    # Det printes hvor mange riktige bevsarelser brukeren har
    print("Antall riktige svar: ",riktige_svar)

# else-setning som printer at brukeren har fått feil, og antall spørsmål besvart bestiges også med én for å gå til neste spørsmål
else:  
    print("Du fikk feil")
    sporsmal_svart += 1
    print("Antall riktige svar: ",riktige_svar)

#####

# if-else funksjonen repeteres for hvert spørsmål
if sporsmal_svart == 1:
   print(" SPØRSMÅL 2 ")
   bruker_sporsmal = input(sporsmol_2)   
else:
   print("Noe gikk feil. Vennligst start på nytt")

if bruker_sporsmal == "a":
    riktige_svar += 1
    print("Riktig! Bra jobbet")
    sporsmal_svart += 1
    print("Antall riktige svar: ",riktige_svar)

else:  
    print("Du fikk feil")
    sporsmal_svart += 1
    print("Antall riktige svar: ",riktige_svar)

#####

# Spørsmål 3

if sporsmal_svart == 2:
   print(" SPØRSMÅL 3 ")
   bruker_sporsmal = input(sporsmol_3)   
else:
   print("Noe gikk feil. Vennligst start på nytt")

if bruker_sporsmal == "å":
    riktige_svar += 1
    print("Riktig!")
    sporsmal_svart += 1
    print("Antall riktige svar: ",riktige_svar)

else:  
    print("Du fikk feil")
    sporsmal_svart += 1
    print("Antall riktige svar: ",riktige_svar)

#####

# Spørsmål 4

if sporsmal_svart == 3:
   print(" SPØRSMÅL 4 ")
   bruker_sporsmal = input(sporsmol_4)   
else:
   print("Noe gikk feil. Vennligst start på nytt")

if bruker_sporsmal == "h":
    riktige_svar += 1
    print("Riktig!")
    sporsmal_svart += 1
    print("Antall riktige svar: ",riktige_svar)

else:  
    print("Du fikk feil")
    sporsmal_svart += 1
    print("Antall riktige svar: ",riktige_svar)

#####

# Spørsmål 5

if sporsmal_svart == 4:
   print(" SPØRSMÅL 5 ")
   bruker_sporsmal = input(sporsmol_5)   
else:
   print("Noe gikk feil. Vennligst start på nytt")

if bruker_sporsmal == "m":
    riktige_svar += 1
    print("Riktig! Så flink du er!")
    sporsmal_svart += 1
    print("Antall riktige svar: ",riktige_svar)

else:  
    print("Du fikk feil :(")
    sporsmal_svart += 1
    print("Antall riktige svar: ",riktige_svar)

#####

# Spørsmål 6

if sporsmal_svart == 5:
   print(" SPØRSMÅL 6 ")
   bruker_sporsmal = input(sporsmol_6)   
else:
   print("Noe gikk feil. Vennligst start på nytt")

if bruker_sporsmal == "u":
    riktige_svar += 1
    print("Riktig!")
    sporsmal_svart += 1
    print("Antall riktige svar: ",riktige_svar)

else:  
    print("Du fikk feil! De heter Ole, Dole og Doffen")
    sporsmal_svart += 1
    print("Antall riktige svar: ",riktige_svar)

#####

# Spørsmål 7

if sporsmal_svart == 6:
   print(" SPØRSMÅL 7 ")
   bruker_sporsmal = input(sporsmol_7)   
else:
   print("Noe gikk feil. Vennligst start på nytt")

if bruker_sporsmal == "n":
    riktige_svar += 1
    print("Riktig!")
    sporsmal_svart += 1
    print("Antall riktige svar: ",riktige_svar)

else:  
    print("Du fikk feil!")
    sporsmal_svart += 1
    print("Antall riktige svar: ",riktige_svar)

#####

# Spørsmål 8

if sporsmal_svart == 7:
   print(" SPØRSMÅL 8 ")
   bruker_sporsmal = input(sporsmol_8)   
else:
   print("Noe gikk feil. Vennligst start på nytt")

if bruker_sporsmal == "n":
    riktige_svar += 1
    print("Riktig!")
    sporsmal_svart += 1
    print("Antall riktige svar: ",riktige_svar)

else:  
    print("Du fikk feil!")
    sporsmal_svart += 1
    print("Antall riktige svar: ",riktige_svar)

#####

# Spørsmål 9

if sporsmal_svart == 8:
   print(" SPØRSMÅL 9 ")
   bruker_sporsmal = input(sporsmol_9)   
else:
   print("Noe gikk feil. Vennligst start på nytt")

if bruker_sporsmal == "n":
    riktige_svar += 1
    print("Riktig!")
    sporsmal_svart += 1
    print("Antall riktige svar: ",riktige_svar)

else:  
    print("Du fikk feil!")
    sporsmal_svart += 1
    print("Antall riktige svar: ",riktige_svar)

#####

# Spørsmål 10

if sporsmal_svart == 9:
   print(" SPØRSMÅL 10 ")
   bruker_sporsmal = input(sporsmol_10)   
else:
   print("Noe gikk feil. Vennligst start på nytt")

if bruker_sporsmal == "u":
    riktige_svar += 1
    print("Riktig! Bra jobbet!")
    sporsmal_svart += 1
    print("Antall riktige svar: ",riktige_svar)

else:  
    print("Du fikk feil!")
    sporsmal_svart += 1
    print("Antall riktige svar: ",riktige_svar)


# Når alle 10 spørsmål har blitt besvart vises brukeren hvor mange rette svar dem fikk, og det blir gitt en tilbakemelding

if riktige_svar < 5:
   print("Godt forsøk! Du fikk",riktige_svar,"ut av 10 riktige")
elif riktige_svar > 5:
   print("Veldig bra! Du fikk",riktige_svar,"ut av 10 riktige svar") 
elif riktige_svar > 8: 
   print("Meget godt besvart! Du fikk",riktige_svar,"ut av 10 riktige svar!")
elif riktige_svar == 10:
   print("Gratulerer! Du fikk",riktige_svar,"ut av 10 riktige svar! Jeg er stolt av deg!")
else:
   print("Oi? Luring, du fikk",riktige_svar,"ut av 10 riktige svar!")