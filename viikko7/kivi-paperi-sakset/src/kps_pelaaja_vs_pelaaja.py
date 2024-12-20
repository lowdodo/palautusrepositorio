from kps import KiviPaperiSakset as KPS


class KPSPelaajaVsPelaaja(KPS):
    def __init__(self, tuomari):
        super().__init__(tuomari)

    def _toisen_siirto(self, ensimmainen_siirto):
        siirto = input("Toisen pelaajan siirto: ")
        return siirto