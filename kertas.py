class Manusia:
    def __init__(self, name, gender, tahun):
        self.name = name
        self.gender = gender
        self.tahun = tahun
    def informasi(self):
        print(f"name {self.name}, gender {self.gender}, tahun lahir {self.tahun}")

manusia1 = Manusia ("bais", "Laki-laki", 2000)
manusia2 = Manusia ("muhit", "Lanang", 1945)

manusia1.informasi()
manusia2.informasi()