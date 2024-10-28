class Buku:
    def __init__(self, judul, tahun, jumlah_halaman, bahan_material, diskon):
        self.judul = judul
        self.tahun = tahun
        self.jumlah_halaman = jumlah_halaman
        self.bahan_material = bahan_material
        self.diskon = diskon

    def getJudul(self):
        return self.judul
    
    def getTahun(self):
        return self.tahun
    
    def getHalaman(self):
        return self.jumlah_halaman
    
    def getMaterial(self):
        return self.bahan_material
    
    def getDiskon(self):
        return self.diskon
    
    def checkHarga(self, tahun_sekarang ):
        harga = 10000
        usia = tahun_sekarang - self.tahun
        if usia <= 5:
            if self.jumlah_halaman <= 100:
                harga = 100000
            elif self.jumlah_halaman > 500:
                harga = 500000
            else:
                harga = 300000
                
        elif usia > 5:
            if self.jumlah_halaman <= 100:
                harga = 50000
            elif self.jumlah_halaman >= 500:
                harga = 250000
            else:
                harga = 150000
        
        harga -= harga * (self.diskon / 100)
        return harga

class Komik(Buku):
    def __init__(self, judul, tahun, jumlah_halaman, bahan_material, diskon, is_colorful):
        super().__init__(judul, tahun, jumlah_halaman, bahan_material, diskon)
        self.is_coloful = is_colorful
        
    def getIs_colorful(self):
        return self.is_coloful


buku1 = Buku("Kalkulus", 2020, 300, "kertas", 20)

komik = Komik("Naruto", 2005, 500, "Kertas", 5, True)

print("judul buku", buku1.getJudul())
print("Tahun terbit", buku1.getTahun())
print("jumlah halaman", buku1.getHalaman())
print("material buku", buku1.getMaterial())
print("harga diskon", buku1.checkHarga(2019))
print("====================================")
print("judul komik", komik.getJudul())
print("Tahun terbit", komik.getTahun())
print("jumlah halaman", komik.getHalaman())
print("material komik", komik.getMaterial())
print("harga diskon", komik.checkHarga(2020))
print("apakah berwarna", komik.getIs_colorful())