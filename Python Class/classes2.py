class Araba():
    def __init__(self,marka,model,yil,hiz,renk):
        self.marka=marka
        self.model=model
        self.yil=yil
        self.hiz=hiz
        self.renk=renk

    def OzellikleriGöster(self):
        print(self.marka)    
        print(self.model)    
        print(self.yil)    
        print(self.hiz)    
        print(self.renk)


araba1=Araba("BMW","740",2019,"350km/h","Mor")
araba2=Araba("Mercedes","A180",2021,"340km/h","Turuncu")

araba1.OzellikleriGöster()
print("----------------------------")
araba2.OzellikleriGöster()


   