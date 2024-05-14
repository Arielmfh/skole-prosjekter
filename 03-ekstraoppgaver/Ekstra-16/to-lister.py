import datetime

# bt_hp er en liste med holdeplasser på en bussrute fra Gulset til Porsgrunn
bt_hp = ["Gulsetsenteret", "Ravnåsen", "Myren", "Skien Landmannstorget", "Rådhusplassen", "Bøle", "Borgestad",
         "Porsgrunn Kammerherreløkka"]

# bt_t er en liste som viser tiden i minutter det tar fra Gulsetsenteret og til aktuell holdeplass.
# Denne listen viser at det tar 6 minutter til Ravnåsen, 11 minutter til Myren, osv.
bt_t = [0, 6, 11, 16, 17, 21, 25, 35]

print("Ny bussrute fra Gulset (M1)")
print("                            ")
start_t = int(input("Oppgi start i timer: "))
start_m = int(input("Oppgi start i minutter: "))
x = datetime.time(start_t, start_m)
tid = x
print("Start tiden er:", tid)
print("                            ")

timer = start_t
minutter = start_m
for i in range(len(bt_t)):

    minutter = minutter + bt_t[i]
    if minutter >= 60:
        timer += 1
        minutter -= 60

    tid = datetime.time(timer, minutter)
    hp = bt_hp[i]
    print("Avgang fra", hp, "kl.", tid)
    minutter = start_m  # Nulstiller minutter
