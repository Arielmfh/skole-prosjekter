import random

# Hele programmet er en uendelig løkke for å generere PIN koder
while True:
    # Input for hvor lang pin koden skal være
    pkode_length = int(input("Hvor langt skal passordet ditt være? "))

    # Sjekker hvis input lengden er mindre eller lik 0
    if pkode_length <= 0:
        # Printer en error melding 
        print("Feil! Koden din er ikke lang nok")
    else:
        # Generer en pin kode med den bestemte lengden
        kode = [str(random.randint(0, 9)) for _ in range(pkode_length)]
        kode = "".join(kode)
        # Printer en fullført melding med den genererte PIN koden
        print("Koden din har blitt laget:", kode)

    # Spør brukeren hvis de vil lage en ny PIN kode
    user_input = input("Vil du lage en ny kode? (ja/nei): ")
    # Sjekker hvis brukeren sin svar er "ja"
    if user_input.lower() != 'ja':
        # Stopper løkken dersom brukeren ikke vil lage en ny pin-kode
        break