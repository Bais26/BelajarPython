class Mobil:
    def __init__(self, merek, model, tahun):
        self.merek = merek
        self.model = model
        self.tahun = tahun

    def tampilkaninfo(self):
        print(f"Mobil; {self.merek} {self.model}, Tahun {self.tahun}")

mobilsaya = Mobil("Toyota", "Camry", 2020)
mobilsaya.tampilkaninfo()