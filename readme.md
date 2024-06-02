class Buku:: Deklarasi kelas Buku sebagai blueprint untuk objek buku.
def __init__(self, judul, pengarang, tahun_terbit):: Konstruktor untuk inisialisasi objek buku dengan atribut judul, pengarang, tahun_terbit, dan status pinjam.
self.dipinjam = False: Inisialisasi atribut dipinjam sebagai False.
def informasi(self):: Metode untuk menampilkan informasi buku, termasuk status pinjam.
def pinjam(self):: Metode untuk meminjam buku.
def kembalikan(self):: Metode untuk mengembalikan buku.
class Perpustakaan:: Deklarasi kelas Perpustakaan untuk mengelola buku-buku.
def __init__(self):: Konstruktor untuk inisialisasi objek perpustakaan dengan daftar buku kosong.
def tambah_buku(self, buku):: Metode untuk menambahkan buku ke daftar perpustakaan.
def cari_buku(self, judul):: Metode untuk mencari buku berdasarkan judul.
def daftar_buku_tersedia(self):: Metode untuk menampilkan daftar buku yang tersedia di perpustakaan.
perpustakaan = Perpustakaan(): Membuat objek perpustakaan.
buku1 = Buku("Python Programming", "John Doe", 2020): Membuat objek buku1.
perpustakaan.tambah_buku(buku1): Menambahkan buku1 ke perpustakaan.
perpustakaan.daftar_buku_tersedia(): Menampilkan daftar buku yang tersedia di perpustakaan.
buku1.pinjam(): Meminjam buku1.
buku2.pinjam(): Meminjam buku2.
buku2.kembalikan(): Mengembalikan buku2.
perpustakaan.daftar_buku_tersedia(): Menampilkan daftar buku yang tersedia setelah beberapa buku dipinjam.