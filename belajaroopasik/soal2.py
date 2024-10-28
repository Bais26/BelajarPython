from datetime import datetime

# Kelas Buku
class Buku:
    def __init__(self, judul, tahun, jumlah_halaman, bahan_material, diskon):
        self.judul = judul
        self.tahun = tahun
        self.jumlah_halaman = jumlah_halaman
        self.bahan_material = bahan_material
        self.diskon = diskon

    def get_judul(self):
        return self.judul

    def get_tahun(self):
        return self.tahun

    def get_jumlah_halaman(self):
        return self.jumlah_halaman

    def get_bahan_material(self):
        return self.bahan_material

    def get_diskon(self):
        return self.diskon

    def set_diskon(self, diskon):
        self.diskon = diskon

    def cek_harga(self):
        harga = 10000  # Harga dasar
        usia = datetime.now().year - self.tahun
        if usia <= 5:
            if self.jumlah_halaman <= 100:
                harga = 100000
            elif self.jumlah_halaman > 500:
                harga = 500000
            else:
                harga = 300000
        elif 5 < usia <= 10:
            if self.jumlah_halaman <= 100:
                harga = 50000
            elif self.jumlah_halaman > 500:
                harga = 250000
            else:
                harga = 150000
        # Diskon
        harga -= harga * (self.diskon / 100)
        return harga


# Kelas Komik
class Komik(Buku):
    def __init__(self, judul, tahun, jumlah_halaman, bahan_material, diskon, is_colorful):
        super().__init__(judul, tahun, jumlah_halaman, bahan_material, diskon)
        self.is_colorful = is_colorful

    def get_is_colorful(self):
        return self.is_colorful

    @staticmethod
    def create_buku(judul, tahun, jumlah_halaman, bahan_material, diskon, is_colorful):
        return Komik(judul, tahun, jumlah_halaman, bahan_material, diskon, is_colorful)


# Buat objek Buku
buku = Buku("Calculus", 2024, 1000, "Kertas", 0)

# Cetak judul buku
print("Judul buku:", buku.get_judul())

# Cek harga buku
print("Harga buku:", buku.cek_harga())

# Buat objek Komik
komik = Komik.create_buku("One Piece", 1998, 500, "Kertas", 0, True)

# Cetak judul buku komik
print("Judul buku komik:", komik.get_judul())
