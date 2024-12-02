KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_maara = 0

    def kuuluu(self, luku):
        on = 0

        if luku in self.ljono:
            on += 1

        if on > 0:
            return True
        return False

    def lisaa(self, n):
        if self.alkioiden_maara == 0:
            self.ljono[0] = n
            self.alkioiden_maara += 1
            return True

        if not self.kuuluu(n):
            self.ljono[self.alkioiden_maara] = n
            self.alkioiden_maara += 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_maara % len(self.ljono) == 0:
                taulukko_old = self.ljono
                self.kopioi_lista(self.ljono, taulukko_old)
                self.ljono = self._luo_lista(self.alkioiden_maara + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.ljono)

            return True

        return False

    def poista(self, n):
        indeksi = -1

        for i in range(0, self.alkioiden_maara):
            if n == self.ljono[i]:
                indeksi = i  # siis luku löytyy tuosta kohdasta :D
                self.ljono[indeksi] = 0
                break

        if indeksi != -1:
            self.ljono.pop(indeksi)
            self.alkioiden_maara -= 1
            return True

        return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_maara

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_maara)

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_maara == 0:
            return "{}"
        elif self.alkioiden_maara == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_maara - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_maara - 1])
            tuotos = tuotos + "}"
            return tuotos
