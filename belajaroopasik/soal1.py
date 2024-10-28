# buat class namanya manusia yang memilikii atribut nama tahun jenis kelamin kemudian buat sebuah object manusia yang object tersebut yang instinceanti memasukan nama t fungsi lagi untuk mengambil nama gender dan tahun lahir
# buat juga pegawai yang memiliki atribut manusia dan pegawai mempunyai atribut nip  selain nip dia juga punya fungsi untuk mangambil nilai nip nya
# buat di class manusia untuk mengecek umur atau usia dimana fungsi tersebut menerima sebuah tahun untuk menghitung usianya

class Manusia:
    def __init__(self, nama, tahun_lahir, jenis_kelamin):
        self.nama = nama
        self.tahun_lahir = tahun_lahir
        self.jenis_kelamin = jenis_kelamin
    
    def ambil_informasi(self):
        print(f"nama: {self.nama}, tahun lahir: {self.tahun_lahir}, jenis kelamin: {self.jenis_kelamin}")

    def checkusia(self, tahun_lahir):
        usia = tahun_lahir - self.tahun_lahir
        if usia > 60:
            return 'tua'
        elif usia < 40:
            return 'muda'
        else:
            return 'sangat muda'
        
ahmad = Manusia('Ahmad', 2000, 'Laki-laki')

ahmad.ambil_informasi()