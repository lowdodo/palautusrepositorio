from tekoaly import Tekoaly
from kps import KiviPaperiSakset as KPS

class KPSTekoaly(KPS):
    def __init__(self, tuomari):
        super().__init__(tuomari)
        self.tekoaly = Tekoaly()


    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto