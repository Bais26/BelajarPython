class Mahasiswa:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai

    def informasi(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}, Nilai: {self.nilai}")

    def tentukan_nilai(self):
        if 90 <= self.nilai <= 100:
            return 'A'
        elif 80 <= self.nilai < 90:
            return 'B'
        elif 70 <= self.nilai < 80:
            return 'C'
        elif 60 <= self.nilai < 70:
            return 'D'
        else:
            return 'E (Tidak Lulus)'

# Contoh penggunaan:
mahasiswa1 = Mahasiswa("John Doe", "123456", 75)
mahasiswa2 = Mahasiswa("Jane Smith", "789012", 92)

print("Informasi Mahasiswa 1:")
mahasiswa1.informasi()
print("Nilai:", mahasiswa1.tentukan_nilai())

print("\nInformasi Mahasiswa 2:")
mahasiswa2.informasi()
print("Nilai:", mahasiswa2.tentukan_nilai())
