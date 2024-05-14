#Importerer alle nødvendige biblioteker
import string

import random

lengde = int(input("Hvor lang vil du at passordet skal være?: "))

# string.printable er en streng med ASCII-tegn som anses som utskrivbare. Dette er en kombinasjon av sifre, ascii_letters, tegnsetting og mellomrom.
passord = ''.join(random.choice(string.printable) for i in range(lengde))

print(passord)
