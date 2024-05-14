# import random
import random

# Variabel for terning 1
terning1 = 0
# Variable for terning 2
terning2 = 1
# variabel for antall kast
antall_kast = 0

# løkke som kaster begge terningene til de har samme verdi
while terning1 != terning2:
    terning1 = random.randint(1, 6)
    terning2 = random.randint(1, 6)
    # for hvert kast telles antall ganger de har blitt kastet
    antall_kast += 1

# det printes verdien til terningene, og hvor mange kast det tok
print("Terningene har verdiene, én:",terning1,"to:",terning2,"Og det tok ",antall_kast,"kast å få disse verdiene.")