# # buat class namanya manusia yang memilikii atribut nama tahun jenis kelamin kemudian buat sebuah object manusia yang object tersebut yang instinceanti memasukan nama t fungsi lagi untuk mengambil nama gender dan tahun lahir
# # buat juga pegawai yang memiliki atribut manusia dan pegawai mempunyai atribut nip  selain nip dia juga punya fungsi untuk mangambil nilai nip nya
# # buat di class manusia untuk mengecek umur atau usia dimana fungsi tersebut menerima sebuah tahun untuk menghitung usianya

# class Manusia:
#     def __init__(self, name, gender, lahir):
#         self.name = name
#         self.gender = gender
#         self.lahir = lahir
#     def getNama(self):
#         return self.name
#     def getGeder(self):
#         return self.gender
#     def getLahir(self):
#         return self.lahir
#     def checkUsia(self, lahir):
#         umur = lahir - self.lahir
#         if umur > 60:
#             return umur, "tua"
#         elif umur > 30:
#             return umur, "muda"
#         else:
#             return umur, "sangat muda"
    
# manusia1 = Manusia ("muhit", "laki", 1998)

# print("nama", manusia1.getNama())
# print("jenis kelamin", manusia1.getGeder())
# print("tahun lahir", manusia1.getLahir)
# print("umur", manusia1.checkUsia(2050))

class Manusia:
    def __init__(self, nama, tahun_lahir, jenis_kelamin):
        self.nama = nama
        self.tahun_lahir = tahun_lahir
        self.jenis_kelamin = jenis_kelamin

    def ambil_informasi(self):
        return f"Nama: {self.nama}\nJenis Kelamin: {self.jenis_kelamin}\nTahun Lahir: {self.tahun_lahir}"


    def check_usia(self, tahun_lahir):
        umur = tahun_lahir - self.tahun_lahir
        if umur > 60:
            return umur, "tua"
        elif umur > 30:
            return umur, "muda"
        else:
            return umur, "sangat muda"

class Pegawai(Manusia):
  def __init__(self, nama, gender, lahir, nip):
    super().__init__(nama, gender, lahir)
    self.nip = nip

  def getNIP(self):
      return self.nip

bais = Pegawai('bais', 'L', 2000, '081234567')
print(bais.ambil_informasi())
print(bais.getNIP())
print("umur",bais.check_usia(2025))

# # Contoh Penggunaan
# andi = Manusia("Andi", 1990, "Laki-laki")
# tahun_sekarang = 2024
# kategori_usia = andi.check_usia(tahun_sekarang)

# print(f"Informasi Manusia:\n{andi.ambil_informasi()}")
# print(f"umur {kategori_usia}")
