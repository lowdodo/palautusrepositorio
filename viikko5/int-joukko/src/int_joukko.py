KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise ValueError("kapasiteetti oltava positiivinen")
        self.kapasiteetti, self.kasvatuskoko = kapasiteetti, kasvatuskoko

        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluuko_listalle(self, n):
        if n in self.ljono:
            return True
        return False

    def lisaa_listalle(self, n):
        if not self.ljono:
            self.ljono.append(n)
            return True

        if not self.kuuluuko_listalle(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm % len(self.ljono) == 0:
                taulukko_old = self.ljono
                self.ljono = self._luo_lista(
                    self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.ljono)
            return True

        return False

    def poista_listalta(self, n):
        try:
            kohta = self.ljono.index(n)
            self.ljono.pop(kohta)
            self.alkioiden_lkm -= 1
            return True
        except ValueError:
            return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def listan_koko(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)
        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        for luku in a.to_int_list():
            x.lisaa_listalle(luku)
        for luku in b.to_int_list():
            x.lisaa_listalle(luku)
        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        for luku in a.to_int_list():
            if luku in b.to_int_list():
                y.lisaa_listalle(luku)
        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        for luku in a.to_int_list():
            if luku not in b.to_int_list():
                z.lisaa_listalle(luku)
        return z

    def __str__(self):
        return "{" + ", ".join(map(str, self.to_int_list())) + "}"
