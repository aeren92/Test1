class Person:
    def __init__(self,firstname,lastname,dateyear):
        self.firstname=firstname
        self.lastname=lastname
        self.dateyear=dateyear
    
    
    def display(self):
        return f"firstname:{self.firstname} lastname:{self.lastname} year:{self.dateyear}"
    
    
    def calculateAge(self):
        return f"Age:{2023-self.dateyear}"
    
    

while True:
    firstname=input("Adinizi giriniz:")
    lastname=input("Soyadinizi giriniz:")
    age=int(input("Dogum Tarihinizi giriniz:"))
    person=Person(firstname,lastname,age)
    print(person.display())
    print(person.calculateAge())
    
    print("Devam etmek istermisiniz (E/H)")
    secim=input()
    
    if secim == 'h' or secim == 'H':
        print("Tesekkür ederiz iyi günler...")
        break
    
    elif secim == 'e' or secim == 'E':
        continue
    
    else :
        print("Yanlis Secim Yaptiniz tekrar deneyiniz !")
        continue
    

    



    

