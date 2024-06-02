# class Nasabah:
#     def __init__(self, nama, saldo):
#         self.nama = nama
#         self.saldo = saldo

#     def cek_saldo(self):
#         return f"Saldo {self.nama}: {self.saldo}"

#     def transfer(self, penerima, jumlah):
#         if jumlah <= 0:
#             return "Jumlah transfer harus lebih dari 0."
#         elif jumlah > self.saldo:
#             return "Saldo tidak mencukupi untuk melakukan transfer."
#         else:
#             self.saldo -= jumlah
#             penerima.saldo += jumlah
#             return f"Transfer berhasil. {self.cek_saldo()}"

# # Contoh penggunaan:
# nasabah1 = Nasabah("John Doe", 1000)
# nasabah2 = Nasabah("Jane Smith", 500)

# print("Sebelum Transfer:")
# print(nasabah1.cek_saldo())
# print(nasabah2.cek_saldo())

# # Melakukan transfer dari nasabah1 ke nasabah2 sejumlah 300
# hasil_transfer = nasabah1.transfer(nasabah2, 300)
# print("\nHasil Transfer:")
# print(hasil_transfer)
# print(nasabah1.cek_saldo())
# print(nasabah2.cek_saldo())

class Nasabah:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo

    def cek_saldo(self):
        return f"Saldo {self.nama}: {self.saldo}"

    def transfer(self, penerima, jumlah):
        if jumlah <= 0:
            return "Jumlah transfer harus lebih dari 0."
        elif jumlah > self.saldo:
            return "Saldo tidak mencukupi untuk melakukan transfer."
        else:
            self.saldo -= jumlah
            penerima.saldo += jumlah
            return f"Transfer berhasil. {self.cek_saldo()}"

# Input nama dan saldo untuk dua nasabah
nama_nasabah1 = input("Masukkan nama Nasabah 1: ")
saldo_nasabah1 = float(input("Masukkan saldo Nasabah 1: "))

nama_nasabah2 = input("Masukkan nama Nasabah 2: ")
saldo_nasabah2 = float(input("Masukkan saldo Nasabah 2: "))

# Membuat objek Nasabah
nasabah1 = Nasabah(nama_nasabah1, saldo_nasabah1)
nasabah2 = Nasabah(nama_nasabah2, saldo_nasabah2)

# Menampilkan saldo awal
print("\nSebelum Transfer:")
print(nasabah1.cek_saldo())
print(nasabah2.cek_saldo())

# Input jumlah transfer
jumlah_transfer = float(input("\nMasukkan jumlah transfer dari Nasabah 1 ke Nasabah 2: "))

# Melakukan transfer
hasil_transfer = nasabah1.transfer(nasabah2, jumlah_transfer)

# Menampilkan hasil transfer dan saldo akhir
print("\nHasil Transfer:")
print(hasil_transfer)
print(nasabah1.cek_saldo())
print(nasabah2.cek_saldo())
