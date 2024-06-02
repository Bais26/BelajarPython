class Mahasiswa:
    def __init__ (mahasiswa, nama, nim, nilai):
        mahasiswa.nama = nama
        mahasiswa.nim = nim
        mahasiswa.nilai = nilai
    def informasi(mahasiswa):
        print(f"Nama: {mahasiswa.nama}, Nim: {mahasiswa.nim}, Nilai: {mahasiswa.nilai}")
    def status(self):
        return self.nilai >= 60
mahasiswa1 = Mahasiswa("John Doe", "123456", 75)
mahasiswa2 = Mahasiswa("Jane Smith", "789012", 60)

print("Informasi Mahasiswa 1:")
mahasiswa1.informasi()
print("Status Kelulusan:", "Lulus" if mahasiswa1.status() else "Tidak Lulus")

print("\nInformasi Mahasiswa 2:")
mahasiswa2.informasi()
print("Status Kelulusan:", "Lulus" if mahasiswa2.status() else "Tidak Lulus")
