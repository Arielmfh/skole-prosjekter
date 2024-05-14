# Importerer MC, Bil og Buss
from Bil import Bil
from Mc import Mc
from Buss import Buss

mc1 = Mc("BMW", 2007, "Blå", "Kardang")
mc1.vis_data()

Bil1 = Bil("Volvo", 2008, "Grå", 4)
Bil1.sett_farge("Grønn")
Bil1.vis_data()

Buss1 = Buss("Volvo", 2011, "Gul", 50)
Buss1.vis_data()
