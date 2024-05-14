# Diverse listeoppgaver
import statistics

# Du skal løse noen oppgaver med denne listen med tall
t = [36,3,8,10,25,37,65,19,29,73,43,41,90,9,93,117,22,66,77,39,1]


# 1. Finn lengden på liste
print("Lengden på listen er: ",len(t))


# 2. Finn minste tallet i lista
minsteTall = min(t)
print("Det minste tallet i listen er: ",minsteTall)


# 3. Finn høyste tallet i lista
hoyTall = max(t)
print("Det høyeste tallet i listen er: ",hoyTall)


# 4. Finn summen av tallene i lista.
sumTall = sum(t)
print("Summen av alle tallene i variabelen er: ",sumTall)




# 5. Finn gjennomsnittet av tallene i lista.
print("Gjennomsnittet av tallene i listen er: ",statistics.mean(t))


# 6. Finn gjennomsnittet til de tre høyeste verdiene i lista.
x = sorted(t, reverse=True)
x = x[:3]
print("Gjenomsnittet av de tre høyeste verdiene er:",statistics.mean(x))

# 7. Lag en funksjon som ganger alle tallene i denne lista tallene med 3.
def gange(Liste):
  nyListe = []
  for x in range (len(Liste)): # repterer for hvert element i listen
    gangeStykke = Liste[x]*3 # ganger elementet i listen med 3
    nyListe.append(gangeStykke)
    print(Liste[x],"ganger 3 er lik ",gangeStykke)# Printer resultatet
  return nyListe 

print(gange(t)) # Ny liste med listen ganger 3

# 8. Lag en funksjon som tar en liste med ord som innparameter og returnerer en annen liste som inneholder lengden av hvert ord.
ord = ["tre","fire","Sturle","å","abcabcabca"]

def listeLengde(l):
  liste = [] # Ny liste for lengden av ordene
  for x in range(len(l)): # Repeterer for hvert ord
   liste.append(len(l[x])) # Legger til lengden til hvert av ordene inn i listen
  return liste

print(listeLengde(ord))


