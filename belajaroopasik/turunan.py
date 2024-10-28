class Kendaraan:
    def __init__(self, jenis):
        self.jenis = jenis

    def tampilkan_jenis(self):
        print(f"Jenis Kendaraan: {self.jenis}")

class Mobil(Kendaraan):
    def __init__(self, merek, model, tahun):
        super().__init__("Mobil")
        self.merek = merek
        self.model = model
        self.tahun = tahun

    def tampilkan_info(self):
        print(f"{self.jenis}: {self.merek} {self.model}, Tahun: {self.tahun}")

mobil_saya = Mobil("Toyota", "Camry", 2020)
mobil_saya.tampilkan_info()  # Output: Mobil: Toyota Camry, Tahun: 2020
