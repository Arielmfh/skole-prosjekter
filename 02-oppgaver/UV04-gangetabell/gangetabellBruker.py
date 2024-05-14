# input bruker tall som integer
bruker_tall = int(input("Hvilket tall vil du gange? "))

# gangetabell variabel for gangestykke
gangetabell_Stykke = 1

# print("her ser du",bruker_tall,"gangen:")
print("Her ser du",bruker_tall,"gangen: ")

# while gangetabell < 11

while gangetabell_Stykke < 11:
    # bruker tall x ganger med gangetabell stykke regnes & printes
    print(bruker_tall,"x",gangetabell_Stykke,"=",bruker_tall * gangetabell_Stykke)
    # gangetabell adderes med +1
    gangetabell_Stykke += 1