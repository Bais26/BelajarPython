class Lingkaran:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitung_luas(self):
        # Rumus luas lingkaran: π * r^2
        return 3.14 * self.jari_jari ** 2

    def hitung_keliling(self):
        # Rumus keliling lingkaran: 2 * π * r
        return 2 * 3.14 * self.jari_jari

# Buat objek lingkaran1 dengan jari-jari 5
lingkaran1 = Lingkaran(5)
print("Lingkaran 1:")
print("Luas:", lingkaran1.hitung_luas())
print("Keliling:", lingkaran1.hitung_keliling())

# Buat objek lingkaran2 dengan jari-jari 7
lingkaran2 = Lingkaran(7)
print("\nLingkaran 2:")
print("Luas:", lingkaran2.hitung_luas())
print("Keliling:", lingkaran2.hitung_keliling())
