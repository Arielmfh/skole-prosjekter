from Hovedkort import Hovedkort
from Skjermkort import Skjermkort
from Lagringsenhet import Lagringsenhet
from Minne import Minne
from Nettverkskontroller import Nettverkskontroller
from Prosessor import Prosessor
from Stromforsyning import Stromforsyning
from Kjolingsenhet import Kjolingsenhet


# Testdata for Hovedkort
mb1 = Hovedkort("ASUS ROG STRIX B550-F", "ASUS", "3 år", "2 000 kr", "ATX", "AM4")
mb2 = Hovedkort("MSI MPG Z690", "MSI", "3 år", "3 500 kr", "ATX", "LGA 1700")

# Testdata for Skjermkort
gpu1 = Skjermkort("GeForce RTX 3080", "NVIDIA", "3 år", "10 000 kr", 4, "7680x4320", 8704, "10 GB GDDR6X")
gpu2 = Skjermkort("Radeon RX 6800 XT", "AMD", "3 år", "9 500 kr", 4, "7680x4320", 4608, "16 GB GDDR6")

# Testdata for Strømforsyning
psu1 = Stromforsyning("Corsair RM750", "Corsair", "3 år", "1 200 kr", 750, "80 Plus Gold", "Modular")
psu2 = Stromforsyning("EVGA 600 BQ", "EVGA", "3 år", "600 kr", 600, "80 Plus Bronze", "Non-modular")

# Testdata for Kjølingsenhet
cooler1 = Kjolingsenhet("Corsair H100i", "Corsair", "3 år", "1 200 kr", "Vannkjøling")
cooler2 = Kjolingsenhet("Noctua NH-D15", "Noctua", "3 år", "900 kr", "Luftkjøling")

# Testdata for Nettverkskontroller
net1 = Nettverkskontroller("ASUS PCE-AX58BT", "ASUS", "3 år", "800 kr", "Wi-Fi 6", "2400 Mbps")
net2 = Nettverkskontroller("TP-Link TG-3468", "TP-Link", "3 år", "300 kr", "Gigabit Ethernet", "1000 Mbps")

# Testdata for Prosessor
cpu1 = Prosessor("Intel Core i7-11700K", "Intel", "3 år", "3 500 kr", 8, "3.6 GHz")
cpu2 = Prosessor("AMD Ryzen 5 5600X", "AMD", "3 år", "2 500 kr", 6, "3.7 GHz")

# Testdata for Lagringsenhet
storage1 = Lagringsenhet("Samsung 970 EVO", "Samsung", "5 år", "1 500 kr", "SSD", "1 TB")
storage2 = Lagringsenhet("Western Digital Blue", "WD", "3 år", "800 kr", "HDD", "1 TB")

# Testdata for Minne
ram1 = Minne("Corsair Vengeance LPX", "Corsair", "3 år", "1 200 kr", "DDR4", "16 GB", "3200 MHz")
ram2 = Minne("G.Skill Trident Z", "G.Skill", "3 år", "1 400 kr", "DDR4", "16 GB", "3600 MHz")

komponenter_liste = []

komponenter_liste.append(mb1)
komponenter_liste.append(mb2)
komponenter_liste.append(psu1)
komponenter_liste.append(psu2)
komponenter_liste.append(cooler1)
komponenter_liste.append(cooler2)
komponenter_liste.append(net1)
komponenter_liste.append(net2)
komponenter_liste.append(cpu1)
komponenter_liste.append(cpu2)
komponenter_liste.append(storage1)
komponenter_liste.append(storage2)
komponenter_liste.append(ram1)
komponenter_liste.append(ram2)
komponenter_liste.append(gpu1)
komponenter_liste.append(gpu2)

for komponent in komponenter_liste:
    komponent.vis_data()