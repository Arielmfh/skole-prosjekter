# input bruker tall som integer
bruker_tall = int(input("Hvilket tall vil du gange? "))

# liste for gangestykkene
ganger = []

# gangetabell variabel for gangestykke
gangetabell_Stykke = 1

# print("her ser du",bruker_tall,"gangen:")
print("Her ser du",bruker_tall,"gangen: ")

# while gangetabell < 11

while gangetabell_Stykke < 11:
    # bruker tall x ganger gangetabell regnes & svaret legges til listen
    ganger.append(bruker_tall * gangetabell_Stykke)
    # gangetabell adderes med +1
    gangetabell_Stykke += 1

# print listen med alle gangestykkene
print(ganger)