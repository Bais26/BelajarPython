# Buatlah kelas dasar RekeningBank dengan atribut pemilik dan saldo. Tambahkan metode informasi() yang mencetak informasi umum tentang rekening.
class RekeningBank:
    def __init__ (self, nama, saldo):
        self.nama = nama
        self.saldo = saldo
    def getName (self):
        return self.nama
    def getSaldo(self):
        return self.saldo
        
# Turunkan dua kelas dari RekeningBank: RekeningTabungan dan RekeningGiro. Setiap kelas turunan harus memiliki atribut tambahan yang sesuai, misalnya bunga untuk RekeningTabungan dan limit untuk RekeningGiro.
class Tabungan(RekeningBank):
    def _init__(self, nama, saldo, bunga):
        super().__init__(nama, saldo)
        self.bunga = bunga
    # def checkBunga(self):
    #     pass

class Giro(RekeningBank):
    def __init__(self, nama, saldo, limit):
        super().__init__(nama, saldo)
        self.limit = limit
    def tarik(self, jumlah):
        if jumlah <= self.saldo + self.limit:
            self.saldo -= jumlah
            return f"Penarikan sebesar {jumlah} berhasil"
        else:
            return "Penarikan Gagal"
    def Sisa(self, tarik):
        return self.saldo - tarik
        
tb1 = RekeningBank("bais",200000)
ts1 = Giro ("bais", 200000,100000)
# print(tb1.getName())
# print(tb1.getSaldo())
print(ts1.getName())
print(ts1.getSaldo())
print(ts1.tarik(400000))
# print(ts1.Sisa())
