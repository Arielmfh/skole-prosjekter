# brukeren oppgir alderen til Henrik og den gjøres om til en integer
henrik_alder = int(input("Vennligst tast inn alderen til Henrik: "))
# brukeren oppgir alderen til Kari og den gjøres om til en integer
kari_alder = int(input("Vennligst tast inn alderen til Kari: "))
print("Henrik sin alder er",henrik_alder)
print("Kari sin alder er",kari_alder)

# betinget funksjon til å finne ut alderforskjeller
# det printes ut hvem som er eldst eller om de er like gamle
if henrik_alder > kari_alder:
    print("Henrik er eldre enn Kari")
elif henrik_alder < kari_alder:
    print("Kari er eldre enn Henrik")
elif henrik_alder == kari_alder:
    print("Henrik og Kari er like gamle")
else:
    print("Noe er feil. Vennligst prøv igjen.")