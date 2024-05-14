import csv
import json
import os
 
 # Vi setter vår current directory til den riktige mappen
os.chdir("02-oppgaver/UV17-Filbehandling/")

print("------->   CSV til Json  <-------")
# Navnet til CSV-filen vi skal konvertere
csv_navn = input("Navnet på CSV filen du vil konvertere til JSON: ")
# Navnet til den nye JSON filen
json_navn = input("Hva skal den nye JSON filen hete: ")
 
 # Vi åpner csv filen som en csv fil
with open(csv_navn + ".csv", newline='') as csvfile:
    # Vi leser  inn data fra csv filen i en reader objekt
    reader = csv.DictReader(csvfile)
    # Dataen blir satt in rad for rad inn i reader
    data = [row for row in reader]
 
 # Dataen blir dumpet inn i en json fil med en indentation som får det til å se oversiktlig ut
with open(json_navn + ".json", 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)
 