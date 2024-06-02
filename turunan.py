from remidi import Manusia
class Pegawai(Manusia):
    def __init__(self, name, gender, year, nip):
        # Manusia.__init__(name, gender, year, nip)
        super().__init__(name, gender, year, nip)
        self.nip = nip
    def getNip(self):
        return self.nip

budi = Pegawai('Budi', 'L',2002,"129217924")
print(budi.getNip)