# importer random
import random

# variabel for antall kast
antall_kast = 0

# variable for terningkasten
terningkast = 0

# løkke som kaster terningen og får et tall mellom 1-6 til den får 6. 
# For hvert kast blir variabelen "kast" addert med én.
while terningkast != 6:
    terningkast = random.randint(1, 6)
    antall_kast += 1

# det printes hvor mange kast det tok å få en sekser
print("Det tok",antall_kast,"kast å få en",terningkast,"med terningen")