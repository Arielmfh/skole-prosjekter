import string

import random

######

#Importerer RegeX
import re

#### Passordgenerator fra Del-2
lengde = int(input("Hvor lang vil du at passordet skal være?: "))

passord = ''.join(random.choice(string.printable) for i in range(lengde))

print(passord)

#################################

# Bruker sitt passord
passord = input("Ditt passord: ")
 
# Pattern variabel som inneholder regulære uttryk som beskriver kravene som passordet må oppfylle
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!])(.{8,})$'
 
# Kontrollorer om passord matcher pattern med hjelp av funksjonen 're.match'
if re.match(pattern, passord):
    #Passordet er komplett og støtter alle kravene
    print("Passord oppfyller kravene.")
else:
    # Passorder matcher ikke pattern
    print("Passord oppfyller kravene; Minst én liten bokstav ('a-z') Minst én stor bokstav ('A-Å') Minst ett siffer ('0-9') Minst ett spesialtegn fra settet '@#$%^&+=!' Passordet må være minst 8 tegn langt. ")