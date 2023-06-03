#Class nedir? Neden Class Kullanırız?
#Class dediğimiz kavram belirli bir araba markasını değil bütün araç kategorilerini kapsar.
#Örnek ulaşım aracı : -> Araba,Helikopter,Gemi,Uçak,Motor

class Araba():
    marka="BMW"
    model="740"
    yil=2019
    hiz="360 km/h"
    renk="Kirmizi"


araba1=Araba()
print("\t\t\tArabanın Özellikleri")    
print(araba1.marka)
print(araba1.model)
print(araba1.yil)
print(araba1.hiz)
print(araba1.renk)