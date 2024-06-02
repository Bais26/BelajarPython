class Buku:
    def __init__(self, judul, tahun, jumlah_halaman, material = "kertas"):
        self.judul = judul
        self.tahun = tahun
        self.halaman = jumlah_halaman
        self.material = material

    def getJudul(self):
        return self.judul
    def getTahun(self):
        return self.tahun
    def getHalaman(self):
        return self.halaman
    def getMaterial(self):
        return self.material
    def checkHarga(self, year):
        usia = year - self.tahun
        if usia <=5 and self.halaman < 100:
            return 100000
        elif usia <= 5 and self.halaman <= 500:
            return 300000
        elif usia <= 5 and self.halaman > 500:
            return 500000
        elif usia <= 10 and self.halaman < 100:
            return 50000
        elif usia <= 10 and self.halaman <= 500:
            return 250000
        elif usia <= 10 and self.halaman > 500:
            return 350000
        else:
            return 10000

class Komik(Buku):
    def __init__(self, judul, tahun, jumlah_halaman, iscolorfull, material="kertas"):
        super().__init__(judul, tahun, jumlah_halaman, material)
        self.warna = iscolorfull
    def checkwarna(self):
        if self.warna:
            return True
        else:
            return False
class Pelajaran(Buku):
    def __init__(self, judul, tahun, jumlah_halaman, cover="soft", material="kertas"):
        super().__init__(judul, tahun, jumlah_halaman, material)
        self.cover = cover
    def getCover(self):
        return self.cover
buku1 = Buku ("apa wis", 2020, 800)
komik1 = Komik ("naruto wis", 2020, 300, True)
pelajaran1 = Pelajaran ("pkn wis", 2020, 800, False)
listbuku = [buku1, komik1, pelajaran1]

for list in listbuku:
    print("judul buku: ", list.getJudul())
    print("tahun: ", list.getTahun())
    print("jumlah halaman: ", list.getHalaman())
    print("Material: ", list.getMaterial())
    print("Harga Buku: ", list.checkHarga(2025))
    print("=" * 20)