from tekoaly_parannettu import TekoalyParannettu
from kps import KiviPaperiSakset as KPS

class KPSParempiTekoaly(KPS):
    def __init__(self, tuomari):
        super().__init__(tuomari)
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        return siirto