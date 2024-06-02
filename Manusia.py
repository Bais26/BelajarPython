# Membuat Class
class Manusia:
  def __init__(self, nama, gender, year, dhuwur=30, abot=3): # Constructor
    self.__name = nama
    self.gender = gender
    self.__year = year
    self.abot = abot
    self.__dhuwur = dhuwur # Private

  def informasi(self):
    print(f'nama {self.__name}, gender {self.gender}, year {self.__year}, duwur {self.__dhuwur}, abot {self.abot}')
    
  def checkUsia(self, year):
    usia = year - self.__year
    if usia > 60:
      return 'Tua'
    elif usia < 40:
      return 'Sangat Muda'
    else:
      return 'Muda'


ahmad = Manusia('Ahmad', 'L', 1990, abot=40)

ahmad.informasi()
print
