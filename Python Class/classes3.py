class daire():
    pi=3.14
    def __init__(self,yaricap=1):
        self.yaricap=yaricap

    def cevreHesap(self):
            return 2*self.pi*self.yaricap

    def  alanHesapla(self):
         return self.pi*(self.yaricap**2)
    
daire1=daire()
daire2=daire(5)
print("Daire 1 Alan ve Çevresi")
print(f'daire hesapla : Alan {daire1.alanHesapla()}')
print(f'cevre hesapla : Cevre {daire1.cevreHesap()}')
print("-----------------------")

print("Daire 2 Alan ve Çevresi")
print(f'daire hesapla : Alan {daire2.alanHesapla()}')
print(f'cevre hesapla : Cevre {daire2.cevreHesap()}')

        