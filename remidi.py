# membuat class
class Manusia:
    def __init__(self, name, gender,year,duwur,bobot):
        self.name = name
        self.gender = gender
        self.year = year
        self.duwur = duwur
        self.bobot = bobot
    def informasi(self):
        print(f"nama: {self.name}, gender: {self.gender}, tahun lahir {self.year} duwur: {self.duwur} bobot: {self.bobot}")

#instantiate (membuat object)
Manusia1 = Manusia("Muhit", "Laki-laki", 1993,100,10)
Manusia2 = Manusia("Bais", "Laki-laki", 1997,100,6)

Manusia1.informasi()
Manusia2.informasi()