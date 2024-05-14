# Pølse pakker. Pølser har 10stk, pølsebrød har 8stk
PolsePakke = 10
PolseBrodPakke = 8

# Hvor mange kommer til festen?
antallPers = int(input("Hvor mange personer kommer til festen? "))
# Hvor mange pølser til hver gjest?
antallSpises = int(input("Hvor mange pølser til hver person? "))

# Variabel som ganger antall personer på antall pølser til hver gjest
polsePerPers = antallPers * antallSpises

# Minste antall pakker som kreves
print("Det trenges minst",polsePerPers // PolsePakke,"pølse pakker!")

# Minimum antall pakker med pølsebrød som kreves
print("Det trenges minst",polsePerPers // PolseBrodPakke,"pølsebrød pakker!")

# Antall pølser som blir til overs
resterendePolser = polsePerPers % PolsePakke
print("Det blir",resterendePolser,"pølser til overs, hvis alle gjestene spiser",antallSpises,"stk!")

# Antall pølsebrød som blir til overs
resterendePolseBrod = polsePerPers % PolseBrodPakke
print("Det blir",resterendePolseBrod,"pølsebrød til overs, hvis alle gjestene spiser",antallSpises,"stk!")

