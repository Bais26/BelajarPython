# Diberikan kelas "Karyawan" dengan atribut nama dan gaji. Buatlah sebuah method untuk menaikkan gaji karyawan sebesar 10%.

# Berikut template kodenya:
# -------------------------------------
class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
    def getNama(self):
        return self.nama
    def getGaji(self):
        return self.gaji
    
    def naik_gaji(self):
        self.gaji *= 1.1

# Gunakan kelas di atas untuk membuat objek karyawan_pertama dengan nama "Budi" dan gaji 5000000
karyawan1 = Karyawan("Budi", 5000000)

# Panggil method untuk menaikkan gaji karyawan_pertama sebesar 10%
# Implementasikan kode di sini
karyawan1.naik_gaji()
# Cetak gaji karyawan_pertama setelah kenaikan
print(karyawan1.getGaji())
print(f"Gaji setelah dinaikkan: {karyawan1.gaji}")
# -----------------------------------------

# Tugas kamu adalah mengimplementasikan method naik_gaji untuk menaikkan gaji sebesar 10%, serta memanggil method tersebut untuk objek karyawan_pertama. Setelah itu, cetak nilai gaji karyawan_pertama setelah kenaikan.