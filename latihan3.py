# class Barang:
#     def __init__ (self, nama, harga, stok):
#         self.nama = nama
#         self.harga = harga
#         self.stok = stok
#     def tampilkan_info(self):
#         print(f"nama {self.nama}, \nharga {self.harga}, \nstok {self.stok}")

# # barang1.tampilkan_info()
# class Transaksi(Barang):
#     def __init__(self, nama, harga, stok, jumlah_barang):
#         super().__init__(nama, harga, stok)
#         self.jumlah_barang = jumlah_barang

#     def hitungTotal(self):
#         self.harga * self.jumlah_barang

# barang1 = Barang("Sabun", 2000, 50)
# barang2 = Barang("Shampoo", 5000, 30)
# barang3 = Barang("Sikat Gigi", 1000, 100)

# transaksi1 = Transaksi("Sabun", 2000, 50, 5)

# transaksi1.hitungTotal()

class Barang:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def tampilkan_info(self):
        print(f"Nama Barang: {self.nama}\nHarga: {self.harga}\nStok: {self.stok}\n")


class Transaksi(Barang):
    def __init__(self, nama, harga, stok, jumlah_barang):
        super().__init__(nama, harga, stok)
        self.jumlah_barang = jumlah_barang

    def hitung_total(self):
        return self.harga * self.jumlah_barang


class Pelanggan:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo

    def proses_transaksi(self, transaksi):
        total_harga = transaksi.hitung_total()
        if total_harga <= self.saldo:
            print(f"Transaksi berhasil! Total harga: {total_harga}")
            self.saldo -= total_harga
            return True
        else:
            print("Saldo tidak mencukupi. Transaksi dibatalkan.")
            return False


class Toko(Pelanggan):
    def __init__(self, nama, saldo):
        super().__init__(nama, saldo)
        self.inventaris_toko = {}

    def tambah_barang(self, barang):
        self.inventaris_toko[barang.nama] = barang


# Contoh Penggunaan
barang1 = Barang("Sabun", 2000, 50)
barang2 = Barang("Shampoo", 5000, 30)
barang3 = Barang("Sikat Gigi", 1000, 100)

transaksi1 = Transaksi("Sabun", 2000, 50, 5)

toko = Toko("Toko ABC", 100000)
toko.tambah_barang(barang1)
toko.tambah_barang(barang2)
toko.tambah_barang(barang3)

for nama_barang, info_barang in toko.inventaris_toko.items():
    info_barang.tampilkan_info()

if toko.proses_transaksi(transaksi1):
    print("Stok setelah transaksi:")
    for nama_barang, info_barang in toko.inventaris_toko.items():
        info_barang.stok -= transaksi1.jumlah_barang
        info_barang.tampilkan_info()

