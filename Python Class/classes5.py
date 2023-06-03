import time

class Kisi():
    def __init__(self,ad,soyad,yas):
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        
    def benKimim(self):
        print(f"Ben bir Kisiyim")
    
    
    def yemek(self,yemek):
        self.yemek=yemek
        print(f'Ben {self.yemek} yiyorum')
    
    
    def icmek(self,icmek):
        self.icmek=icmek
        print(f'Ben {self.icmek} iciyorum')
    
    
    def kosmak(self,kosmak):
        self.kosmak=kosmak
        print(f'Ben {self.kosmak} kosuyorum')
        
    
    def dusunmek(self,dusunmek):
        self.dusunmek=dusunmek
        print(f'Ben {self.dusunmek} düşünüyorum')




class Ogrenci(Kisi):
    def __init__(self, ad, soyad, yas,ogrenci):
        super().__init__(ad, soyad, yas)
        self.ogrenci = ogrenci                            
    
    
    def benKimim(self):
        print(f"Ben bir Kisiyim")
    
    
    def yemek(self,yemek):
        self.yemek=yemek
        print(f'Ben {self.yemek} yiyorum')
    
    
    def icmek(self,icmek):
        self.icmek=icmek
        print(f'Ben {self.icmek} iciyorum')
    
    
    def kosmak(self,kosmak):
        self.kosmak=kosmak
        print(f'Ben {self.kosmak} kosuyorum')
        
    
    def dusunmek(self,dusunmek):
        self.dusunmek=dusunmek
        print(f'Ben {self.dusunmek} düşünüyorum')


class Ogretmen(Kisi):
    def __init__(self, ad, soyad, yas,ogretmen):
        super().__init__(ad, soyad, yas)
        self.ogretmen = ogretmen
        
    def benKimim(self):
        print(f"Ben bir Kisiyim")
    
    
    def yemek(self,yemek):
        self.yemek=yemek
        print(f'Ben {self.yemek} yiyorum')
    
    
    def icmek(self,icmek):
        self.icmek=icmek
        print(f'Ben {self.icmek} iciyorum')
    
    
    def kosmak(self,kosmak):
        self.kosmak=kosmak
        print(f'Ben {self.kosmak} kosuyorum')
        
    
    def dusunmek(self,dusunmek):
        self.dusunmek=dusunmek
        print(f'Ben {self.dusunmek} düşünüyorum')



print("Lütfen diger kisini bilgilerini bekleyiniz...")
time.sleep(3)


kisi1=Kisi('Derya','Ozer','26')
kisi1.benKimim()
print(kisi1.ad+'\n'+kisi1.soyad+'\n'+kisi1.yas)
kisi1.yemek("Doner")
kisi1.icmek("Kola")

print("Lütfen diger kisini bilgilerini bekleyiniz...")
time.sleep(3)

print("---------------------------------")
ogrenci=Ogrenci('Deniz','Guzelyurt','18','12-A Sinifinda Bir Ogrenci !')
ogrenci.benKimim()
print(ogrenci.ad+'\n'+ogrenci.soyad+'\n'+ogrenci.yas+'\n'+ogrenci.ogrenci)
ogrenci.yemek("Adana porsiyon")
ogrenci.icmek("Şalgam")
ogrenci.kosmak("Avrasya Maratonu")
ogrenci.dusunmek("Kaybolan gençligini")
                                  
                                  
                                  
print("Lütfen diger kisini bilgilerini bekleyiniz...")
time.sleep(3)                              
                                  
print("---------------------------------")
ogrenci2=Ogrenci('Emre','Mor','23','Üniversite 3. Sinifinda Bir Ogrenci !')
ogrenci2.benKimim()
print(ogrenci2.ad+'\n'+ogrenci2.soyad+'\n'+ogrenci2.yas+'\n'+ogrenci2.ogrenci)
ogrenci2.yemek("Urfa porsiyon")
ogrenci2.icmek("Kola")
ogrenci2.kosmak("Orman")
ogrenci2.dusunmek("Araba Almayi")                                  