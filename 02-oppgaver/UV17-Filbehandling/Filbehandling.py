import csv

with open('02-oppgaver/UV17-Filbehandling/ansatte.csv', 'r') as csv_file:
    leser = csv.DictReader(csv_file)

    # Oppgave 1
    antall_kvinner = 0
    antall_menn = 0
    # Oppgave 2
    total_lonn = 0
    antall_ansatte = 0
    #Oppgave 3
    lonn_kvinner = 0
    # Oppgave 4
    lonn_menn = 0

    for row in leser:
        # Oppgave 1
        if row['kjonn'] == 'kvinne':
            antall_kvinner += 1
            # Oppgave 3
            lonn_kvinner += int(row['lonn'])
        else: #row['kjonn'] == 'mann':
            antall_menn += 1
            # Oppgave 4
            lonn_menn += int(row['lonn'])
        # Oppgave 2    
        total_lonn += int(row['lonn'])
        antall_ansatte += 1    

    # Oppgave 1 resultater
    print("Antall kvinner: ",antall_kvinner)
    print("Antall menn: ",antall_menn) 
    # Oppgave 2 resultater
    gjennomsnittslonn = total_lonn / antall_ansatte
    print("Gjennomsnittslønnen er: ",gjennomsnittslonn)
    # Oppgave 3
    if antall_kvinner > 0: # Vi unngår å dele på null hvis det ikke er noen kvinner
        gjennomsnittslonn_kvinner = lonn_kvinner / antall_kvinner
        print(f"Gjennomsnittslønn for kvinner: {gjennomsnittslonn_kvinner}")
    else:
        print("Ingen kvinner i filen.")
    # Oppgave 4
    if antall_menn > 0: # Vi unngår å dele på null hvis det ikke er noen menn
        gjennomsnittslonn_menn = lonn_menn / antall_menn
        print(f"Gjennomsnittslønn for kvinner: {gjennomsnittslonn_menn}")
    else:
        print("Ingen menn i filen.")    