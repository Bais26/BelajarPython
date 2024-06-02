class Buku:
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.dipinjam = False

    def informasi(self):
        status_pinjam = "Tersedia" if not self.dipinjam else "Dipinjam"
        print(f"{self.judul} - {self.pengarang} ({self.tahun_terbit}) - {status_pinjam}")

    def pinjam(self):
        if not self.dipinjam:
            self.dipinjam = True
            print(f"Buku '{self.judul}' berhasil dipinjam.")
        else:
            print(f"Buku '{self.judul}' sudah dipinjam.")

    def kembalikan(self):
        if self.dipinjam:
            self.dipinjam = False
            print(f"Buku '{self.judul}' berhasil dikembalikan.")
        else:
            print(f"Buku '{self.judul}' belum dipinjam.")

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
        print(f"Buku '{buku.judul}' ditambahkan ke perpustakaan.")

    def cari_buku(self, judul):
        for buku in self.daftar_buku:
            if buku.judul.lower() == judul.lower():
                return buku
        return None

    def daftar_buku_tersedia(self):
        print("Daftar Buku Tersedia:")
        for buku in self.daftar_buku:
            if not buku.dipinjam:
                buku.informasi()


# Contoh penggunaan:
# Membuat objek perpustakaan
perpustakaan = Perpustakaan()

# Menambahkan beberapa buku ke perpustakaan
buku1 = Buku("Python Programming", "John Doe", 2020)
buku2 = Buku("Data Science Basics", "Jane Smith", 2019)
buku3 = Buku("Web Development Guide", "Sam Johnson", 2021)

perpustakaan.tambah_buku(buku1)
perpustakaan.tambah_buku(buku2)
perpustakaan.tambah_buku(buku3)

# Menampilkan daftar buku yang tersedia
perpustakaan.daftar_buku_tersedia()

# Peminjaman dan pengembalian buku
buku1.pinjam()
buku2.pinjam()
buku2.kembalikan()

# Menampilkan kembali daftar buku yang tersedia setelah beberapa buku dipinjam
perpustakaan.daftar_buku_tersedia()
