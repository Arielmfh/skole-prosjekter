# input for kjøpsum som skal betales
betalingsum = int(input("Hvor mye skal betales? "))
# Printer kjøpe sum i kroner
print("Kjøpe sum: kr",betalingsum,",-")

# En annen variabel som lagrer betalingsummen 
mengdePenger = betalingsum

# input kontantsedler du skal betale med
kontanter = int(input("Hvor mye penger skal du betale med? "))

if betalingsum > kontanter:
    print("Du kan ikke kjøpe noe du ikke har råd til!")
else:
# Print som forteller hvor mye du betaler med
 print("Betaler med: Kr",kontanter,",-")

#print for tomrom
print(" ")
#Print som forteller kunden kontantene de bruker
print("Kjøpets Kontanter")

#print for tomrom
print(" ")
 # Kunden sine kontanter regnes til heltall og moduleres for å vise antall sedler & kontanter som blir brukt i kjøpet
AntallTusenLapper = mengdePenger // 1000
mengdePenger = mengdePenger % 1000
print(AntallTusenLapper,"stk tusen-lapper")

AntallFemHundreLapper = mengdePenger // 500
mengdePenger = mengdePenger % 500
print(AntallFemHundreLapper,"stk femhundre-lapper")

AntallToHundreLapper = mengdePenger // 200
mengdePenger = mengdePenger % 200
print(AntallToHundreLapper,"stk to-hundre-lapper")

AntallHundreLapper = mengdePenger // 100
mengdePenger = mengdePenger % 100
print(AntallHundreLapper,"stk hundre-lapper")

AntallFemtiLapper = mengdePenger // 50
mengdePenger = mengdePenger % 50
print(AntallFemtiLapper,"stk femti-lapper")

tjuekronemynter = mengdePenger // 20
mengdePenger = mengdePenger % 20
print(tjuekronemynter,"stk 20-krone-mynt")

tikronemynter = mengdePenger // 10
mengdePenger = mengdePenger % 10
print(tikronemynter,"stk 10-krone-mynt")

femkronemynter = mengdePenger // 5
mengdePenger = mengdePenger % 5
print(femkronemynter,"stk 5-krone-mynt")

enkronemynter = mengdePenger // 1
mengdePenger = mengdePenger % 1
print(enkronemynter,"stk 1-krone-mynt")

#print for tomrom
print(" ")
# Variabel for resterende penger. Kontanter regnes med betalingsummen for å få vekselen.
resterendePenger = kontanter % betalingsum
# Resterende penger printes ut til kunden
print("Penger tilbake til kunden: kr",resterendePenger,",-")

#print for tomrom
print(" ")
# Print som forteller kunden resterende kontanter de får tilbake
print("Resterende kontanter")

#print for tomrom
print(" ")
# Kunden sine resterende kontanter regnes til heltall og moduleres for å vise hvilke kontanter de får tilbake
AntallTusenLapper = resterendePenger // 1000
resterendePenger = resterendePenger % 1000
print(AntallTusenLapper,"stk tusen-lapper")

AntallFemHundreLapper = resterendePenger // 500
resterendePenger = resterendePenger % 500
print(AntallFemHundreLapper,"stk femhundre-lapper")

AntallToHundreLapper = resterendePenger // 200
resterendePenger = resterendePenger % 200
print(AntallToHundreLapper,"stk to-hundre-lapper")

AntallHundreLapper = resterendePenger // 100
resterendePenger = resterendePenger % 100
print(AntallHundreLapper,"stk hundre-lapper")

AntallFemtiLapper = resterendePenger // 50
resterendePenger = resterendePenger % 50
print(AntallFemtiLapper,"stk femti-lapper")

tjuekronemynter = resterendePenger // 20
resterendePenger = resterendePenger % 20
print(tjuekronemynter,"stk 20-krone-mynt")

tikronemynter = resterendePenger // 10
resterendePenger = resterendePenger % 10
print(tikronemynter,"stk 10-krone-mynt")

femkronemynter = resterendePenger // 5
resterendePenger = resterendePenger % 5
print(femkronemynter,"stk 5-krone-mynt")

enkronemynter = resterendePenger // 1
resterendePenger = resterendePenger % 1
print(enkronemynter,"stk 1-krone-mynt")