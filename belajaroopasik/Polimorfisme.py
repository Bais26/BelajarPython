class Hewan:
    def suara(self):
        pass

class Kucing(Hewan):
    def suara(self):
        return "Meow"

class Anjing(Hewan):
    def suara(self):
        return "Bark"

hewan_list = [Kucing(), Anjing()]
for hewan in hewan_list:
    print(hewan.suara())  # Output: Meow, Bark
