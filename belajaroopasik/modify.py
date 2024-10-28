class AkunBank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.__saldo = saldo  # Atribut private

    def deposit(self, jumlah):
        self.__saldo += jumlah

    def tampilkan_saldo(self):
        print(f"Saldo: {self.__saldo}")

akun = AkunBank("Budi", 100000)
akun.deposit(50000)
akun.tampilkan_saldo()  # Output: Saldo: 150000
